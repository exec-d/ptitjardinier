"""Valide les fiches plantes publiées.

Le schéma JSON couvre la forme. Ce script couvre ce qu'un schéma ne sait pas
dire : qu'un identifiant de fichier corresponde à son contenu, qu'une ancre
geste-precedent — qu'elle apparaisse au premier niveau des gestes d'une
fiche ou dans un enchaînement « declenche » — pointe un geste qui existe
réellement dans la fiche, et que le vocabulaire des ancres n'ait pas grossi
en douce. La troisième vérification est la plus importante : le pari du
projet est que sept ancres suffisent, et une huitième ajoutée sans décision
le perdrait sans que personne ne le remarque.
"""

import json
import sys
from pathlib import Path

import jsonschema

ANCRES_ATTENDUES = {
    "derniere-gelee", "premiere-gelee", "degres-jours",
    "temperature-glissante-7j", "photoperiode", "dormance",
    "geste-precedent", "date-civile",
}


def tous_les_gestes(gestes):
    """Aplatit l'arbre des gestes d'une fiche : premier niveau et
    enchaînements (« declenche ») confondus, à toute profondeur."""
    for geste in gestes:
        yield geste
        yield from tous_les_gestes(geste.get("declenche", []))


def ancres_utilisees(gestes):
    for geste in tous_les_gestes(gestes):
        yield geste["quand"]["ancre"]


def main() -> int:
    racine = Path(__file__).resolve().parent.parent
    schema = json.loads((racine / "schema/fiche.schema.json").read_text())

    declarees = set(schema["$defs"]["quand"]["properties"]["ancre"]["enum"])
    if declarees != ANCRES_ATTENDUES:
        print(f"le vocabulaire des ancres a changé : {declarees ^ ANCRES_ATTENDUES}")
        print("l'élargir est une décision de conception, pas un ajout de routine")
        return 1

    fautes = []
    fiches = sorted((racine / "plants").glob("*.json"))
    fiches = [f for f in fiches if f.name != "index.json"]
    if not fiches:
        print("aucune fiche trouvée : le chemin est faux ou le dépôt est vide")
        return 1

    for chemin in fiches:
        fiche = json.loads(chemin.read_text())
        try:
            jsonschema.validate(fiche, schema)
        except jsonschema.ValidationError as e:
            fautes.append(f"{chemin.name} : {e.message}")
            continue

        if fiche["id"] != chemin.stem:
            fautes.append(f"{chemin.name} : id « {fiche['id']} » ≠ nom de fichier")

        tous = list(tous_les_gestes(fiche["gestes"]))
        connus = {geste["type"] for geste in tous}
        for geste in tous:
            cible = geste["quand"].get("geste")
            if cible is not None and cible not in connus:
                fautes.append(
                    f"{chemin.name} : geste-precedent pointe « {cible} », absent"
                )

    for faute in fautes:
        print(faute)
    print(f"{len(fiches)} fiches, {len(fautes)} fautes")
    return 1 if fautes else 0


if __name__ == "__main__":
    sys.exit(main())
