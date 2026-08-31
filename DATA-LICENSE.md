# Licences et attribution des données publiées dans ce dépôt

Chaque fiche de `plants/` mélange trois natures de contenu, qui n'ont ni la même origine ni la
même licence : un squelette botanique factuel, des gestes et conseils rédigés ici, et — une fois
affichés par l'application, pas publiés dans ce dépôt — des données climatiques et un référentiel
communal hérités d'un autre dépôt du même projet. Le code de ce dépôt s'y ajoute comme une
quatrième catégorie, à part : ce n'est pas du contenu. Cette page les couvre dans cet ordre.

## Squelette botanique — noms latins, familles, cycles

Les champs `nomLatin`, `famille` et `cycle` de chaque fiche proviennent de
[Wikidata](https://www.wikidata.org), sous licence
[CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/deed.fr) (dédicace au domaine
public). CC0 ne requiert aucune attribution ; Wikidata est cité ici par traçabilité, pas par
obligation de licence.

## Gestes, conseils et paramètres agronomiques — rédigés dans ce dépôt

Le reste de chaque fiche — rusticité minimale (`rusticiteMinC`), besoin d'ensoleillement
(`heuresSoleilMin`), préférences de sol (`sol`), et surtout les gestes (`gestes`), leurs
conditions de déclenchement (`quand`, `conditions`) et leurs conseils (`conseil`) — est écrit par
les contributeurs de ce dépôt à partir de sources horticoles publiques, dans leurs propres mots,
avec renvoi aux sources plutôt que reprise de leur texte. Ce n'est pas une compilation
automatique : chaque fiche cite ses sources dans son propre champ `sources` (titre, URL, date de
consultation), et porte un niveau de `confiance` (`verifie` ou `a-relire`) qui dit si cette
synthèse a été relue.

**Licence de ce contenu original : [Creative Commons Attribution-ShareAlike 4.0 International
(CC BY-SA 4.0)](https://creativecommons.org/licenses/by-sa/4.0/deed.fr).**

Pourquoi CC BY-SA plutôt qu'une licence de base de données comme l'ODbL (celle qu'utilise par
exemple `exec-d/terminus-32` pour ses données GTFS redistribuées) : ces fiches ne sont ni une
redistribution ni une compilation dérivée d'une base de données existante, mais du contenu
original rédigé dans ce dépôt. L'ODbL répond à une question différente (protéger une base de
données) et n'est donc pas le cadre pertinent ici.

CC BY-SA impose deux choses à qui reprend une fiche, en tout ou en partie : **créditer** ce
dépôt comme source, et **republier ses propres modifications sous la même licence** (partage à
l'identique) — pour qu'une correction ou une amélioration faite ailleurs profite aux suivants
plutôt que de se refermer.

**Attribution demandée** : mentionner « P'tit Jardinier », un lien vers
[`exec-d/ptitjardinier`](https://github.com/exec-d/ptitjardinier), et indiquer les modifications
apportées si le contenu repris a été changé.

**Texte de la licence** : reproduit intégralement dans [`LICENSE`](LICENSE) à la racine de ce
dépôt (texte juridique complet, tel que publié par Creative Commons). Version de référence en
ligne : [résumé en français](https://creativecommons.org/licenses/by-sa/4.0/deed.fr) et
[texte juridique complet](https://creativecommons.org/licenses/by-sa/4.0/legalcode).

Cette licence couvre uniquement les champs listés au début de cette section. Elle ne couvre ni
le squelette botanique (CC0, section précédente), ni les mentions climatiques héritées (section
suivante), ni le code de ce dépôt (dernière section).

## Mentions climatiques et référentiel communal — héritées de `exec-d/plusdsaison`

L'application affiche des données climatiques et un référentiel de communes qui ne sont **pas**
publiés dans ce dépôt : ils viennent de
[`exec-d/plusdsaison`](https://github.com/exec-d/plusdsaison), qui impose ses propres
attributions obligatoires. Ce qui suit est **rédigé ici** pour présenter chaque source ; seuls
les **blocs cités** (encadrés `>`) et le DOI sont repris **verbatim** depuis `DATA-LICENSE.md` de
`exec-d/plusdsaison` (consulté le 2026-08-31) — ce sont eux les mentions obligatoires, et c'est
leur exactitude qui compte. En cas de divergence future entre les phrases de présentation
ci-dessous et le contenu réel de `exec-d/plusdsaison`, ce sont les mentions de
`exec-d/plusdsaison` qui font foi. Ces mentions ne sont **pas** couvertes par la licence CC BY-SA
de la section précédente : Copernicus, Météo-France et l'IGN imposent leurs propres conditions,
indépendantes de ce que ce dépôt choisit pour son propre contenu.

### Copernicus Climate Change Service (C3S) — ERA5-Land

Les séries climatiques quotidiennes sont dérivées du jeu **ERA5-Land daily statistics** du
Copernicus Climate Change Service (C3S), distribué par le Climate Data Store — DOI
[10.24381/cds.e9c9c792](https://doi.org/10.24381/cds.e9c9c792). Les précipitations proviennent du
jeu **ERA5-Land hourly** du même service.

> Generated using Copernicus Climate Change Service information 2026.
> Ni la Commission européenne ni l'ECMWF ne sont responsables de l'usage fait de ces données.

### Météo-France

Les écarts mesurés entre les données climatiques et les stations sont calculés à partir des
**Données climatologiques de base quotidiennes** de **Météo-France**, diffusées sur
[meteo.data.gouv.fr](https://meteo.data.gouv.fr) sous
[Licence Ouverte 2.0](https://www.etalab.gouv.fr/licence-ouverte-open-licence/).

> Contient des données de Météo-France diffusées via meteo.data.gouv.fr, sous Licence Ouverte 2.0.

### geo.api.gouv.fr et IGN — RGE ALTI®

Le référentiel communal (code officiel géographique, centroïdes) vient de
[geo.api.gouv.fr](https://geo.api.gouv.fr), sous Licence Ouverte. L'altitude de chaque commune
vient du service altimétrique de la [Géoplateforme IGN](https://geoservices.ign.fr), qui expose
le **RGE ALTI®** sous [Licence Ouverte 2.0](https://www.etalab.gouv.fr/licence-ouverte-open-licence/).

> Contient des données de l'IGN — RGE ALTI®, sous Licence Ouverte 2.0.

## Code de ce dépôt

`tools/*.py` (le validateur, le générateur d'index) et `.github/workflows/` ne sont pas du
contenu : ce sont des outils. Ils ne relèvent ni de CC BY-SA (contenu des fiches), ni de CC0
(squelette botanique), ni des licences climatiques ci-dessus. **Leur licence n'a pas été
tranchée** ; ce document ne leur applique aucune des licences décrites plus haut, et
`LICENSE` à la racine ne couvre — voir sa propre note de périmètre — que le contenu original des
fiches.

---

Application non officielle, non affiliée à Météo-France, au Copernicus Climate Change Service, à
l'ECMWF, à l'IGN ni à geo.api.gouv.fr. Les erreurs qu'elle contiendrait sont les siennes.
