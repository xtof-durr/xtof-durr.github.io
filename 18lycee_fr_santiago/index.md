# Jeux alternés

Deux joueurs, jouent à tour de rôle. Graphe des configurations. Configurations gagnantes et perdantes. Déterminer type de configuration de manière récursive en partant des configuration finales.

Le jeux de la tablette de chocolat. Preuve que la configuration initale est gagnante par vol de stratégie.

## Le jeux hexapawn

Introduit par Richard Gardner en 1962. Illustre de manière simplifié l'apprentissage des ordinateurs.

- [matériel](hexapawn/hexapawn.pdf) distribué aux étudiants. En plus il faut 24 coupelles et une 15-zaine de perles de chacune des couleurs rouge, jaune, vert et bleu.

## Bonus: Le graphe de jeu de morpion

Le nombre de configurations possibles est 3^9 = 19 683, car il y a 3 valeurs possibles pour chacune des 3*3 cases. Par contre seulement certaines configurations peuvent apparaître dans un jeu, par exemple il est impossible d'avoir trois croix et trois ronds alignés dans une même configuration.

Pour réduire ce nombre d'avantage, on peut groupes les configurations symmétriques. On finit par avoir 765 noeuds dans l'arbre de jeu. C'est encore trop grand pour être visualisable.

- [code qui génère le graphe du jeu](morpion/morpion.py)