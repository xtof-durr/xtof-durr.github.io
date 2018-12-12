---
title: Éléments de correction pour le devoir maison
---

École Centrale-Supélec - parcours Informatique et Systèmes Avancés - [Tronc commun](http://www.isia.ecp.fr/welcome_to_www_ecp_fr_cms_site_isia/isia___formation/cours_tronc_commun) - cours IS3005AD: Algorithmique Avancée

## Commentaires sur Exo 1

Écrit à la main ou à la machine n'a pas d'importance, mais mettez des numéros
de page (le convertisseur markdown vers PDF *pandoc* les ajoute par défaut)
et surtout mettez votre nom sur la première page, SVP. Pour ceux qui ont codé
en C++, C# ou Rust, j'ai juste inspecté attentivement le code. Les autres
projets en Python ont subi un test systématique avec plusieurs instances
aléatoires de tailles différentes, par ce [programme](optimal_search_tree.py)
de test.  Il est important que vous donniez le code dans un fichier texte, pas
inclu dans un document PDF.  Ici les indices pouvaient débuter par 0 ou 1, je
me suis adapté. Mais il était important de suivre les consignes, en
particulier de produire un tableau comme demandé, et de fournir
une fonction avec la signature demandée. Si vous avez seulement traduit
l'algorithme de Knuth votre travail n'était pas complet.  Concernant la
qualité du code, il est important de le commenter, et de dire pour chaque
fonction ce qu'elle fait, pour chaque variable ce qu'elle représente. Un code
est destiné à la lecture d'un humain également.


## Commentaires sur Exo 2
La solution consiste à décomposer la matrice en une matrice $A$ avec les parties entières et un autre 
matrice $B$ avec les parties décimales. Ensuite il faut arrondir la matrice $B$ en une matrice 0-1. L'idée est de construire un graphe bipartie dont les sommets correspondent aux lignes et colonnes de la matrice $B$, et deux sommets supplémentaire $s$ et $t$ (similaire ce qu'on a vue dans le TD). Chaque arête entre $s$ et un sommet ligne a une capacité égale à la valeur totale de la ligne dans la matrice $B$. Chaque arête entre $t$ et un sommet colonne a une capacité égale à la valeur totale de la colonne dans la matrice $B$. Puis, chaque arête entre un sommet colonne et un sommet ligne a une capacité 1 si l'élément dans l'intersection entre la colonne et la ligne est de valeur positive; 0 sinon.

Le reste est d'évoquer l'algorithme Edmonds-Karps et justifier comment on peut obtenir la solution entière demandée dans l'exercice. 

Une approche que quelques étudiants ont suivi est de considérer les bornes inférieurs et supérieures sur les capacités des arêtes. Dans litérature, il existe un algorithme qui retourne une solution qui satisfait ces contraintes. Cependant, cet algorithme est plus sophistiqué et n'est pas enseigné dans le cadre du cours. Par conséquent, si on utilise cette approche, il faut donner et expliquer l'algorithme qui traite les bornes inférieurs et supérieures (et bien sûr prouver que la solution retournée est bien celle qu'on souhaite). 


## Remark     

Plusieurs étudiants ont rendu un devoir quasi-parfait, aussi je pense que vous pourriez les
contacter pour comparer avec ce que vous avez rendu.  Leurs noms sont Armand
Bouvier-Neveu, Rémi Garde, Gabriel Moneyron, Romain Pascual, Kylian Serrania et Yiren Wang.


