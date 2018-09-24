---
title: Corrigé
---

École Centrale-Supélec - parcours Informatique et Systèmes Avancés - [Tronc commun](http://www.isia.ecp.fr/welcome_to_www_ecp_fr_cms_site_isia/isia___formation/cours_tronc_commun) - cours IS3005AD: Algorithmique Avancée

## Plus grand carré dans une grille

Notons A[i,j] la longueur du côté du plus grand carré tout blanc qui ait comme coin en bas à droit la case (i,j). On dira que le carré est ancré en (i,j).

### Observation clé

Si la case (i,j) est noire on a forcément A[i,j]=0, Sinon
considérons une case (i,j) avec A[i,j]=k et k ≥ 1. Alors le carré de côté k ancré en (i,j) contient trois carrés blancs de côté k-1, ancrés respectivement en (i,j-1), (i-1,j) et (i-1,j-1).  On a donc A[i,j-1] ≥ k-1, mais également A[i-1,j]≥k-1 et A[i-1,j-1]≥k-1. En d'autres termes

\\( A[i,j] \leq 1 + \min\{ A[i, j-1], A[i-1,j]. A[i-1,j-1]\}. \\)

Mais l'intersection des carées blancs ancrés en ces trois cases et des côtés respectifs A[i, j-1], A[i-1,j]. A[i-1,j-1], complété par la case (i,j) constitue un carré blanc de côté \\(1 +  \min\{ A[i, j-1], A[i-1,j]. A[i-1,j-1]\}\\).  Nous avons done la récursion

\\( A[i,j] = 1 + \min\{ A[i, j-1], A[i-1,j]. A[i-1,j-1]\}, \\)

pour toute case (i,j) blanche et i,j>1.  En résumé:

### Cas de base

Pour la première ligne et première colonne, les carrés sont de côté 0 ou 1 suivant la couleur de la case. Donc

\\[ \forall (i,j): i=1 \vee j=1 \Rightarrow A[i,j]=
\left\{
\begin{array}{ll}
0 & \mbox{ si la case (i,j) est noire } \\
1 & \mbox{ si la case (i,j) est blanche } \\
\end{array}
\right.
\\]

### Récursion

\\[ \forall (i,j): i,j>1 \Rightarrow A[i,j]=
\left\{
\begin{array}{ll}
0 & \mbox{ si la case (i,j) est noire } \\
1+\min\{A[i, j-1], A[i-1,j]. A[i-1,j-1]\} & \mbox{ sinon } \\
\end{array}
\right.
\\]

## Plus long chemin dans un arbre

On veut calculer pour chaque sous-arbre enraciné en un sommet v le plus long chemin dans ce sous-arbre.  
Notons A[v] cette longueur.

Calculons d'abord la profondeur de l'arbre. La profondeur est égale à la longueur du plus long chemin qui a v comme extrémité, et une feuille la plus éloignée de v comme autre extrémité.  Notons Prof[v] la profondeur.

Maintenant un plus long chemin P dans le sous-arbre enraciné en v, soit passe par v, soit ne passe pas par v.  Dans le dernier cas il est inclu dans un des sous-arbres des descendants directs de v.  Le premier cas se décompose en deux sous-cas.
Soit v a un seul fils, alors la longueur de P est forcément Prof[v].
Soit v a plusieurs fils, alors dans P v a deux voisins, disons u1 et u2. Et le chemin débute sur une feuille du sous-arbre enraciné en u1, passe par u1,v,u2 puis continue vers une feuille du sous-arbre enraciné en u2.
On a donc les récursions suivantes. 

### Cas de base: v est une feuille

Prof[v] =0, A[v] = 0

### Récursion pour v ayant un seul fils u

Prof[v] = 1  + Prof[u].
A[v] = max{ A[u], Prof[v] }

### Récursion pour v ayant plusieurs fils

Prof[v] = 1  + Prof[u].
A[v] = max{ A[u], Prof[u1] + 2 + Prof[u2] },
où u1,u2 sont deux descendants de v de profondeur maximale.

## Jeux avec des pièces alignées

Notons A[i,j] le plus grand score un joueur peut atteindre s'il est celui qui commence sur la configuration composée des pièces entre les indices i et j. Alors
A[i,i] = p[i] clairement. Et pour i < j, A[i,j] est l'optimum sur les deux possibilités du premier coup, à savoir:

A[i,j] = p[i] + ... + p[j] - min{A[i,j-1, A[i+1,j]]}.

## Pavage par des dominos

Fixez un pavage. Considérez la frontière entre deux colonnes j et j+1 de la grille.  Pour chacune des trois lignes, elle peut être traversée par un domino ou pas. Notons par un mot de \\(\{0,1\}^3\\) cette configuration, avec 1 représentant une traversée.  Il y a 8 configurations possibles.  

### Compatibilité des configurations

On peut décrire une matrice binaire M de dimension 8 fois 8, où M[x,y]=1 s'il existe un pavage où la frontière entre les colonnes j et j+1 soit dans la configuration x et celle entre les colonnes j+1 et j+2 dans la configuration y.
Alors \\(M^n(000,000)\\) est le nombre demandé.  

La matrice \\(M^n\\) peut être obtenue par exponentiation rapide en faisant \\(\log n\\) multiplications de matrices.

Par contre les valeurs de la matrice \\(M^n\\) seront très grand, et nécessitent de l'ordre de n bits pour leur représentation.  Pour une analyse raisonable on devrait donc abandonner le modèle où chaque opération arithmétique coûte un temps constant, et considérer un modèle où on compte les opérations sur les bits.  Actuellement le meilleur algorithme de multiplication de matrice connue sur des entiers sur n bits a une complexité de \\(O(n\log n 2^{\log^* n})\\), ce qui en pratique est proche de \\(O(n\log n)\\). Bien qu'il y ait \\O(\log n)\\) multiplications d'entiers, comme leur longueur suit une série géométrique, le dernier terme domine et  \\(O(n\log n 2^{\log^* n})\\) est la complexité de l'algorithme qui calcule le nombre de pavages d'une grille 3 fois n par des dominos.
