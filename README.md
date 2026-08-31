# P'tit Jardinier — catalogue de plantes

P'tit Jardinier est une application de jardinage sans backend. Ce dépôt est sa partie données :
un fichier JSON par espèce, dont les gestes portent des **conditions** — « semer six semaines
avant la dernière gelée, quantile 80 % » — plutôt que des dates en dur. L'application résout ces
conditions sur l'appareil, contre le climat réel de la commune de l'utilisateur, tel que publié
par [`exec-d/plusdsaison`](https://github.com/exec-d/plusdsaison).

## Ce que contient le dépôt

- **`plants/*.json`** — une fiche par espèce, conforme à `schema/fiche.schema.json`. Chaque fiche
  porte un squelette botanique factuel (nom latin, famille, cycle), une liste de `gestes` ancrés
  plutôt que datés, ses `sources`, et un niveau de `confiance` (`verifie` ou `a-relire`).
- **`plants/index.json`** — le catalogue léger, régénéré : `id`, `nomsFr`, `nomLatin`, `famille`,
  `categorie`, `confiance` de chaque fiche. C'est ce que l'application télécharge pour chercher
  dans le catalogue sans rapatrier toutes les fiches complètes.
- **`manifest.json`** — `format_version`, `n_fiches`, `updated`. Ce que l'application relit en
  premier pour savoir si son cache OTA est à jour ; `format_version` invalide le cache de tous
  les clients installés quand il est incrémenté.
- **`schema/fiche.schema.json`** — la forme d'une fiche, dont le vocabulaire **fermé** des sept
  ancres possibles pour un geste (`derniere-gelee`, `premiere-gelee`, `degres-jours`,
  `temperature-glissante-7j`, `photoperiode`, `dormance`, `geste-precedent`, `date-civile`).
- **`tools/valider.py`** — valide chaque fiche contre le schéma, vérifie que l'`id` correspond au
  nom de fichier, que les enchaînements `geste-precedent` pointent un geste qui existe, et que le
  vocabulaire des ancres n'a pas grossi sans décision explicite.
- **`tools/construire_index.py`** — régénère `plants/index.json` et `manifest.json` à partir des
  fiches. Voir `.github/workflows/valider.yml` : la CI échoue si le résultat commité diverge de ce
  que ce script produirait.
- **`docs/verdict-ancres.md`** — le verdict, écrit en éprouvant le vocabulaire des sept ancres sur
  trois fiches délibérément difficiles (pommier, rosier, ail), sur le fait qu'il suffise.
- **`DATA-LICENSE.md`** — les licences et attributions, jeu de données par jeu de données.
- **`LICENSE`** — texte complet de la licence CC BY-SA 4.0 qui couvre le contenu original des
  fiches (voir `DATA-LICENSE.md` pour le périmètre exact).

## Comment l'application l'utilise

Aucun serveur : l'application télécharge ce dépôt en statique (`raw.githubusercontent.com`), ce
qui suppose un dépôt public. Elle lit d'abord `manifest.json`, puis `plants/index.json` pour la
recherche, et ne télécharge une fiche complète qu'à l'ouverture. Chaque geste d'une fiche porte
une ancre plutôt qu'une date ; l'application la résout contre le profil de saison de la commune
choisie, calculé depuis les séries climatiques de `exec-d/plusdsaison`.

Le catalogue grandit par simple ajout de fiches OTA, sans nouvelle version de l'application.

## Le catalogue est incomplet — assumé, pas une excuse

Ce dépôt contient à ce stade **23 fiches** : trois fiches d'épreuve écrites pour éprouver le
vocabulaire des sept ancres avant de figer le format — pommier (`malus-domestica`, verger),
rosier (`rosa`, ornement), ail (`allium-sativum`, potager) — voir `docs/verdict-ancres.md` —
et vingt fiches potager qui forment la première couverture réelle (aromatique et fruitier
restent, pour l'instant, uniquement représentés par basilic et pommier). **Toutes les 23**
sont encore `"confiance": "a-relire"`, sans exception.

C'est un engagement du projet, pas une limite provisoire qu'on cache : l'application **assume et
affiche** que sa couverture est partielle plutôt que de laisser croire à un catalogue complet. Le
verger et l'ornemental restent très peu couverts, et s'ajoutent après coup, en continu, sans
jamais viser un lot initial exhaustif.

## Valider et régénérer localement

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r tools/requirements.txt

python tools/valider.py            # schéma + invariants + vocabulaire des ancres
python tools/construire_index.py   # régénère plants/index.json et manifest.json
```

Après toute modification de `plants/`, régénérer et commiter `plants/index.json` et
`manifest.json` avec les fiches : la CI (`.github/workflows/valider.yml`) échoue si le résultat
commité ne correspond plus à ce que produirait `tools/construire_index.py` — un index périmé
ferait disparaître des fiches de la recherche sans qu'aucune erreur ne le signale.

## Licences

Ce dépôt mélange plusieurs licences, pas une seule : le contenu original des fiches (gestes,
conseils, paramètres agronomiques) est sous **CC BY-SA 4.0** (texte complet dans
[`LICENSE`](LICENSE)), le squelette botanique importé de Wikidata reste **CC0**, et les
mentions climatiques et communales affichées par l'application mais héritées de
`exec-d/plusdsaison` gardent leurs propres licences et leurs attributions obligatoires. Le code
de ce dépôt (`tools/`, workflows) n'entre dans aucune de ces catégories ; sa licence n'a pas été
tranchée. Le détail, jeu par jeu, est dans [`DATA-LICENSE.md`](DATA-LICENSE.md) — à lire avant
de réutiliser quoi que ce soit de ce dépôt.

---

Application non officielle. Les erreurs qu'elle contiendrait sont les siennes.
