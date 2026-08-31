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
import sys
from datetime import date
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


def construire_manifeste(n_fiches: int, aujourdhui: date) -> dict:
    return {
        "format_version": FORMAT_VERSION,
        "n_fiches": n_fiches,
        "updated": aujourdhui.isoformat(),
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
    manifeste = construire_manifeste(len(fiches), date.today())

    ecrire_json(racine / "plants" / "index.json", index)
    ecrire_json(racine / "manifest.json", manifeste)

    print(f"index et manifeste régénérés : {len(fiches)} fiches")
    return 0


if __name__ == "__main__":
    sys.exit(main())
