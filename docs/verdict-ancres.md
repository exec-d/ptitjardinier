# Verdict : le vocabulaire des sept ancres tient-il ?

Trois fiches ont été écrites pour éprouver le pari du projet — pommier
(`malus-domestica`), rosier (`rosa`), ail (`allium-sativum`) — avant les
trente fiches faciles. Ce document répond franchement à la question posée
par la tâche 10 : sept ancres suffisent-elles, sans repli sur
`date-civile` ?

## Verdict en une phrase

**Oui, les sept ancres ont suffi aux trois cas, sans qu'aucun geste ne soit
replié sur `date-civile` faute de mieux** — mais un mécanisme voisin des
ancres, la récurrence d'un `geste-precedent`, montre une limite qui n'est
pas une question de vocabulaire d'ancre et qu'il faut documenter honnêtement
plutôt que passer sous silence.

Aucune des neuf occurrences de `quand.ancre` dans les trois fiches n'utilise
`date-civile`. C'est le résultat le plus important de cette tâche : le cas
conçu pour faire craquer le vocabulaire — l'ail, dont la bulbaison répond à
la durée du jour et non à la température — s'exprime proprement avec
`photoperiode`, sans triche.

## Ce que chaque fiche a éprouvé

### Pommier — `dormance` et l'enchaînement `geste-precedent`

Trois gestes, fournis verbatim par le brief : `taille-hiver` (ancre
`dormance`, phase `debut`, décalage de 21 jours après la chute des
feuilles), `eclaircissage` (ancre `degres-jours`, seuil 250), et
`taille-vert` chaîné sur `eclaircissage` via `geste-precedent` (45 jours
après). Aucune friction : les trois ancres utilisées correspondent
exactement aux gestes réels de la conduite d'un pommier tels que documentés
par la RHS et les guides d'arboriculture consultés.

### Rosier — `dormance` à l'autre bout, et la remontance

Le rosier réutilise `dormance`, mais à l'**autre extrémité** de la fenêtre :
`phase: "fin"` avec un décalage négatif (tailler juste avant le
débourrement, quand les bourgeons gonflent), contre `phase: "debut"` pour
le pommier (tailler juste après la chute des feuilles). C'est une
confirmation utile : le champ `phase` de l'ancre `dormance` n'est pas un
détail cosmétique, il permet à une seule ancre de couvrir deux pratiques
d'arboriculture opposées (tailler tôt en dormance vs. tailler tard en
dormance) sans dupliquer le vocabulaire.

La floraison remontante, en revanche, a résisté davantage. Supprimer les
fleurs fanées relance une nouvelle vague de floraison sous 6 à 8 semaines
(source : Pépinières Dima), et ce geste se répète ensuite **à chaque
nouvelle floraison, indéfiniment jusqu'à l'automne** — grossièrement toutes
les trois semaines selon Jardiner Malin. `geste-precedent` exprime
proprement la *première* occurrence (chaînée sur `taille-dormance`), mais
rien dans le vocabulaire actuel n'exprime « puis recommence après
toi-même » : un `geste-precedent` qui pointerait sur son propre type serait
structurellement étrange dans un schéma pensé pour des chaînes finies
(`declenche`), pas pour une boucle. J'ai contourné en confiant la
récurrence au champ `conseil` (texte, pas donnée structurée) — ce qui
fonctionne pour informer le jardinier mais ne permettra pas à l'application
de programmer un rappel pour la 2ᵉ, 3ᵉ, 4ᵉ floraison de la saison de la même
façon que pour la 1ʳᵉ.

**Ce n'est pas un trou dans le vocabulaire des sept ancres** — aucune des
sept ne manque pour dater cette floraison remontante, `geste-precedent`
est le bon choix conceptuel. C'est une limite de la façon dont les gestes
s'enchaînent (une chaîne finie, pas une boucle), orthogonale à la question
posée par cette tâche. Je le signale parce que la tâche demande « tout
geste que tu as eu du mal à exprimer » ; je ne propose pas de le corriger
ici, ce n'est pas non plus une décision de vocabulaire d'ancre.

### Ail — `photoperiode`, le cas qui devait faire craquer le vocabulaire

Le geste central, `arret-arrosage`, s'ancre sur `photoperiode` avec un
seuil de 13 heures de jour : passé ce seuil, l'ail cesse de produire des
feuilles et concentre son énergie dans le bulbe, un mécanisme confirmé par
la littérature scientifique (Wu et al. 2016, revue à comité de lecture) et
indépendant de la température ou de la date. C'est précisément le geste que
le brief attendait de cette fiche, et il s'exprime sans effort avec
l'ancre prévue pour ça.

Les deux autres gestes utilisent des combinaisons jusque-là inemployées par
le pommier : `plantation` combine `premiere-gelee` avec `quantile` (0.5) et
un `decalageJours` négatif — la seule occurrence de `quantile` dans les
trois fiches, ce qui valide que ce champ du schéma sert à quelque chose de
réel (planter par rapport à une date de gel *probable*, pas fixe).
`recolte` chaîne sur `arret-arrosage` via `geste-precedent`.

Un point mérite d'être noté sans en faire un problème d'ancre : le vrai
signal de récolte de l'ail est **visuel** (proportion de feuilles jaunies),
pas calculable depuis une donnée météo. `geste-precedent` donne une bonne
estimation du moment (21 jours après l'arrêt de l'arrosage, sourcé), mais
le `conseil` renvoie explicitement au jardinier la confirmation visuelle.
Aucune des sept ancres ne couvre — et n'a vocation à couvrir — un signal
phénologique observé à l'œil ; ce sera vraisemblablement vrai pour beaucoup
d'autres gestes de récolte futurs (tomates mûres, courges qui sonnent
creux...). Ce n'est pas propre à l'ail, ce n'est pas un manque à combler
dans le vocabulaire des ancres.

## `dormance` : l'ancre la plus faible, et pourquoi

`dormance` est utilisée trois fois dans ces fiches (deux fois pour le
pommier et le rosier au niveau du geste, implicitement dans la façon dont
l'application devra un jour calculer « début » et « fin » de la dormance).
Cette tâche ne spécifie **pas** quel modèle de calcul de froid l'ancre doit
utiliser — c'est un choix d'implémentation qui reste ouvert, hors du
périmètre du format de fiche lui-même. Mais il faut documenter que ce choix
n'est pas neutre :

- La levée de dormance dépend d'une **accumulation de froid** (« chill »)
  propre à chaque espèce et variété, avant que l'arbre ne puisse répondre à
  la chaleur du printemps pour débourrer (INRAE, 17 décembre 2024).
- Plusieurs modèles concurrents existent pour quantifier ce froid — le
  modèle Utah (heures de froid pondérées, avec « négation » du froid par
  les températures douces) et le modèle Dynamique (accumulation en deux
  étapes, en « Chill Portions ») étant les deux principaux.
- Ces modèles **ne s'accordent pas entre eux**, en particulier en climat
  doux : Luedeling & Brown (2010, *International Journal of
  Biometeorology*) montrent que le modèle Utah produit des totaux de froid
  négatifs et inutilisables dans les régions subtropicales, et que « les
  modèles ne sont donc pas proportionnels : un besoin en froid déterminé à
  un endroit peut ne pas être valide ailleurs » (traduction).

Conséquence concrète pour P'tit Jardinier : le jour où `dormance.debut` et
`dormance.fin` seront effectivement calculés (hors périmètre de cette
tâche), le choix du modèle sous-jacent devra être explicite et documenté,
et son incertitude assumée — particulièrement dans les régions à hiver
doux où les modèles divergent le plus. Cette tâche ne tranche pas ce choix ;
elle documente qu'il existe et qu'il n'est pas anodin.

## Ce que je ne recommande pas de faire maintenant

Aucune fiche n'a eu besoin d'une huitième ancre. Je ne propose donc
**aucun ajout au vocabulaire**. La seule friction réelle rencontrée (la
remontance du rosier) n'est pas un problème d'ancre mais de chaînage de
gestes — une question de conception différente, que je signale sans y
toucher, conformément à la consigne de la tâche.

## Conclusion

Le pari tient sur les trois cas les plus durs choisis précisément pour le
faire échouer. L'ail — le cas conçu pour ça — n'a pas eu besoin de
`date-civile`. Les trois fiches restent en `"confiance": "a-relire"` : ce
verdict porte sur le vocabulaire, pas sur l'exactitude horticole de chaque
paramètre numérique, qui reste à relire par un humain (voir le rapport de
tâche pour le détail des sources consultées et des affirmations non
sourcées).
