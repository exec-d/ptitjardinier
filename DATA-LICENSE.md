# Licences et attribution des données publiées dans ce dépôt

Chaque fiche de `plants/` mélange trois natures de contenu, qui n'ont ni la même origine ni la
même licence : un squelette botanique factuel, des gestes et conseils rédigés ici, et — une fois
affichés par l'application, pas publiés dans ce dépôt — des données climatiques et un référentiel
communal hérités d'un autre dépôt du même projet. Cette page les couvre dans cet ordre.

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
les contributeurs de ce dépôt à partir de sources horticoles publiques. Ce n'est pas une
compilation automatique : chaque fiche cite ses sources dans son propre champ `sources` (titre,
URL, date de consultation), et porte un niveau de `confiance` (`verifie` ou `a-relire`) qui dit
si cette synthèse a été relue.

**Licence de ce contenu original : non encore déterminée.** Ce point n'a pas été tranché dans
cette tâche — voir le rapport de tâche 11a pour les options proposées et pourquoi la décision
revient à l'utilisateur. Tant qu'aucune licence n'est choisie et affichée ici, ce contenu reste
par défaut sous droit d'auteur classique (« tous droits réservés »), comme toute œuvre de
l'esprit sans licence explicite.

## Mentions climatiques et référentiel communal — héritées de `exec-d/plusdsaison`

L'application affiche des données climatiques et un référentiel de communes qui ne sont **pas**
publiés dans ce dépôt : ils viennent de
[`exec-d/plusdsaison`](https://github.com/exec-d/plusdsaison), qui impose ses propres
attributions obligatoires. Les mentions ci-dessous sont reprises **verbatim** depuis
`DATA-LICENSE.md` de ce dépôt (section par section), consulté le 2026-08-31 ; en cas de
divergence future, ce sont les mentions de `exec-d/plusdsaison` qui font foi.

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

---

Application non officielle, non affiliée à Météo-France, au Copernicus Climate Change Service, à
l'ECMWF, à l'IGN ni à geo.api.gouv.fr. Les erreurs qu'elle contiendrait sont les siennes.
