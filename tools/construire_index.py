"""Construit l'index léger du catalogue et le manifeste du dépôt.

L'index (`plants/index.json`) est ce que l'application télécharge pour
proposer une recherche sans rapatrier toutes les fiches complètes : de quoi
identifier une plante et savoir si sa fiche est encore « à relire », sans le
détail des gestes. Le manifeste (`manifest.json`, à la racine) est ce que
l'application relit en premier pour savoir si son cache OTA est à jour —
`format_version` en est la clé : l'incrémenter force tous les clients
installés à retélécharger, même si le contenu n'a par ailleurs pas changé.

Ce script régénère les deux fichiers en entier à chaque exécution : le
catalogue est trop petit pour justifier une mise à jour incrémentale. La CI
le relance après validation et échoue si le résultat diffère de ce qui est
commité (voir `.github/workflows/valider.yml`) : un index périmé fait
disparaître silencieusement des fiches de la recherche, sans qu'aucune
erreur ne le signale ailleurs, donc il ne doit jamais pouvoir dériver de son
contenu source.
"""

import json
import subprocess
import sys
from datetime import date, datetime, timezone
from pathlib import Path

# Incrémenter à chaque changement de forme de index.json ou manifest.json
# (ajout, retrait ou renommage d'un champ) : comme chez plusdsaison, c'est
# ce qui invalide le cache de tous les clients installés.
FORMAT_VERSION = 1

# Les seuls champs qu'un client doit lire pour chercher dans le catalogue
# sans télécharger la fiche complète. L'ordre fixe l'ordre des clés dans
# chaque entrée de l'index.
CHAMPS_INDEX = ("id", "nomsFr", "nomLatin", "famille", "categorie", "confiance")


def charger_fiches(racine: Path) -> list[dict]:
    chemins = sorted((racine / "plants").glob("*.json"))
    chemins = [c for c in chemins if c.name != "index.json"]
    return [json.loads(chemin.read_text()) for chemin in chemins]


def construire_index(fiches: list[dict]) -> list[dict]:
    entrees = [{champ: fiche[champ] for champ in CHAMPS_INDEX} for fiche in fiches]
    return sorted(entrees, key=lambda entree: entree["id"])


def date_dernier_commit_plants(racine: Path) -> date:
    """Date (UTC) du dernier commit qui a touché plants/ — la donnée que le
    manifeste décrit, pas l'horloge du poste qui le régénère.

    date.today() a été essayé et a produit un faux échec de CI en
    production : un manifeste régénéré localement un soir, puis régénéré
    par la CI le lendemain matin, sans qu'aucune fiche n'ait changé entre
    les deux, ne contenait plus la même date. Un manifeste dont le contenu
    change sans que la donnée change est faux ; il doit être reproductible
    (régénérer deux fois sans rien changer doit produire deux fois le même
    fichier), ce que seule une donnée dérivée de l'historique — et non de
    l'instant de régénération — peut garantir.

    Échoue bruyamment plutôt que de retomber en silence sur date.today() si
    la date ne peut pas être obtenue de façon fiable (dépôt git absent,
    historique tronqué par un clone superficiel, ou vraiment aucun commit
    ne touchant encore plants/) : un repli silencieux réintroduirait
    exactement le défaut qu'on corrige ici.
    """
    resultat = subprocess.run(
        ["git", "log", "-1", "--format=%ct", "--", "plants/"],
        cwd=racine, capture_output=True, text=True,
    )
    sortie = resultat.stdout.strip()
    if resultat.returncode != 0 or not sortie:
        raise RuntimeError(
            "impossible de déterminer la date du dernier commit touchant "
            "plants/ (dépôt git absent, historique tronqué — un clone CI a "
            "besoin de fetch-depth: 0 — ou aucun commit ne touche encore "
            "plants/). Pas de repli silencieux sur l'horloge du jour : "
            "corriger la source plutôt que deviner la date."
        )
    return datetime.fromtimestamp(int(sortie), tz=timezone.utc).date()


def construire_manifeste(n_fiches: int, mise_a_jour: date) -> dict:
    return {
        "format_version": FORMAT_VERSION,
        "n_fiches": n_fiches,
        "updated": mise_a_jour.isoformat(),
    }


def ecrire_json(chemin: Path, contenu) -> None:
    chemin.write_text(json.dumps(contenu, indent=2, ensure_ascii=False) + "\n")


def main() -> int:
    racine = Path(__file__).resolve().parent.parent
    fiches = charger_fiches(racine)
    if not fiches:
        print("aucune fiche trouvée : le chemin est faux ou le dépôt est vide")
        return 1

    index = construire_index(fiches)
    manifeste = construire_manifeste(len(fiches), date_dernier_commit_plants(racine))

    ecrire_json(racine / "plants" / "index.json", index)
    ecrire_json(racine / "manifest.json", manifeste)

    print(f"index et manifeste régénérés : {len(fiches)} fiches")
    return 0


if __name__ == "__main__":
    sys.exit(main())
