---
title: Devoir maison
---

École Centrale-Supélec - parcours Informatique et Systèmes Avancés - [Tronc commun](http://www.isia.ecp.fr/welcome_to_www_ecp_fr_cms_site_isia/isia___formation/cours_tronc_commun) - cours IS3005AD: Algorithmique avancée


Les deux parties sont à faire et à rendre pour le mercredi 17 octobre à [cette page](http://www-desir.lip6.fr/~durrc/Iut/rendre/).  Seront noté l'exactitude, la précision et la présentation.  La note comptera pour 40% dans votre évaluation.

## Partie sur la programmation dynamique


On veut stocker $n$ éléments comparables dans un arbre binaire de recherche.
Pour simplifier on suppose que les éléments sont les entiers de $1$ à $n$.
On pourrait pour cela prendre un arbre binaire équilibré, ce qui garantirait des temps d'accès dans le pire des cas de $O(\log n)$.  Mais on s'intéresse à optimiser le temps d'accès moyen, pour des fréquences d'accès $f[1\ldots n]$ données pour chaque élément.
Concrètement si $p[i]$ est la profondeur de l'élément $i$ dans l'arbre produit alors on veut minimiser la somme $\sum_{i=1}^n f[i]\cdot p[i]$.
Pour fixer les choses on dira que la racine a la profondeur $1$, les descendants directs de la racine ont la profondeur $2$ et ainsi de suite.

Nous avons vu un algorithme par programmation dynamique de complexité $O(n^3)$.
En 1971 Donald Knuth a publié un algorithme de meilleure complexité $O(n^2)$.

1. Comprenez l'algorithme proposé par D. Knuth. [Optimum Binary Search Trees, D. E. KNUTH , Acta Informatica 1, 14-25 (1971) ](http://www.inrg.csie.ntu.edu.tw/algorithm2014/presentation/Knuth71.pdf)
2. Expliquez l'algorithme formellement en pseudo-code et prouver l'optimalité de la solution produite.
3. Implémentez l'algorithme dans le langage de programmation de votre choix. 

Concrètement vous devriez implémenter une fonction qui prend en paramètre un tableau de fréquences et qui retourne un arbre optimal de recherche sous forme d'un tableau qui contient pour chaque indice i, l'indice du parent dans l'arbre ou simplement i, dans le cas où i est la racine de l'arbre.

Si vous programmez en Python, donnez seulement le code de cette fonction. Si vous programmez en un autre langage donnez un programme complet qui lit à partir de l'entrée standard l'entier n, puis les n fréquences, ces n+1 entiers étant séparés par des espaces, et terminant par un retour charriot.  Ce programme affichera ensuite dans la sortie standard les n nombres codant l'arbre.

## Partie sur les flots

On vous donne une matrice A[1..m][1..n] de nombres fractionnels non-négatifs.  Votre but est d'arrondir A vers une matrice entière B, en remplaçant chaque entrée $x$ de $A$ par $\lceil x\rceil$  ou par $\lfloor x\rfloor$, en préservant les sommes sur les entrées de toutes les lignes et de toutes les colonnes.  Pour cela on supposera que les sommes de toutes les colonnes et de toutes les lignes de $A$ sont entières.
Par exemple


		entrée                 sortie
		[ 1.2  3.4  2.4 ]      [ 1   4   2 ]
		[ 3.9  4    2.1 ]  ->  [ 4   4   2 ]
		[ 7.9  1.6  0.5 ]      [ 8   1   1 ]

1. Montrez comment ce problème peut être réduit à un problème de flot.
2. Montrez qu'il existe toujours une solution.

