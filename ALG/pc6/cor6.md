---
title: Corrigé
---

École Centrale-Supélec - parcours Informatique et Systèmes Avancés - [Tronc commun](http://www.isia.ecp.fr/welcome_to_www_ecp_fr_cms_site_isia/isia___formation/cours_tronc_commun) - cours IS3005AD: Algorithmique Avancée

## Subset Sum

Soit $\langle G(V,E),k\rangle$ une instance de Vertex Cover.
On numérote les arêtes de $e_0$ à $e_{m-1}$ pour $m=|E|$, et les sommets $v_0, \ldots,v_{n-1}$ pour $n=|V|$.
Chaque sommet $v_j$ génère le nombre 
\\[
     a_j := 10^m + \sum_{v_j\in e_i} 10^i,
\\]
et chaque arrête $e_i$ génère le nombre
\\[
     a_{n+i} := 10^i,
\\]
Remarques que dans la notation décimale de chacun des nombres, il n'y a que les chiffres 0 ou 1 dans les $m$ positions les moins significatives.
Soit $B = k \cdot 10^m + \sum_{i=0}^{m-1} 2 \cdot 10^i$,
donc le nombre $k$ en notation décimale suivi de $m$ fois le chiffre 2.

On va montrer qu'il existe un ensemble $T\subseteq \{0,n+m-1\}$ tel que $\sum_{i\in T} a_i = B$ ssi il existe un ensemble $S\subset V$ avec $|S|=k$ qui couvre chaque arête.

### $\Rightarrow$

Soit $T\subseteq \{0,n+m-1\}$ tel que $\sum_{i\in T} a_i = B$.
Soit $S = \{v_j: 0\leq j \leq n-1, j\in T\}$.
Comme il n'y a pas de retenu dans les $m$ chiffres les moins significatives, et que la valeur cible a le ciffre 2 en ces positions, $S$ doit contenir pour chaque arête $e_i=(v_j, v_{j'})$ au moins un des entiers $j,j'$ et donc $S$ est une couverture par sommets. De plus comme il n'y a pas de retenu dans la somme $\sum_{i\in T} a_i$ dans les $m$ positions les moins significatives, et comme cette somme est au moins $k 10^k$, on a $|S|=k$.

### $\Leftarrow$

Soit $S\subseteq V$ une couverture par sommets de taille $k$. On pose $T=\{j:v_j\in S\}$ qu'on complète par $n+i$ pour toute arête $e_i$ qui n'a qu'une des extrémités dans $S$. Une vérification mécanique montre que $\sum_{i\in T} a_i = B$.

### base 3

On aurait pu faire cette construction également avec la base 3 au lieu de 10.  Dans ce cas il faut montrer que pour une solution $T \{0,n+m-1\}$ on a que pour tout $e_i=(v_j,v_{j'})$, $T$ contient $j$ ou $j'$ (ou les deux). Par induction sur les positions des chiffres dans la somme $\sum_{i\in T} a_i$. Considérons la position $i$. Par hypothèse d'induction il n'y a pas eu de retenu de la position $i-1$ vers la position $i$.  Donc la seule manière d'obtenir un $2$ en cette position est par au moins un $0\leq j\leq n-1$ dans $T$ avec $v_j$ étant une extrémité de $e_i$. Et dans ce cas la position $i$ ne provoque pas de retenue vers la position $i+1$.

## 2-Partition

On considère une instance $\langle S,B \rangle$ de SUBSET-SUM, et on crée un ensemble $S'$, instance de 2-Partition. 
Notons $\sum S$ la somme eniters de $S$.  Sans perte de généralité et par symétrique supposons que $B \leq \sum S / 2$.
Tout simplement $S'$ sera $S$ plus un entier supplémentaire, à savoir $\sum S-2B$. 

Supposons que $S'$ admet une partition en deux parties de même taille. Considérons celui qui contient l'entier supplémenaire. Soit $x$ la somme des autres entiers de cette partie.  La somme des entiers de l'autre partie est alors $\sum S -x$.
Comme $S'$ est une 2-Partition, on a l'égalité $\sum S-2B + x = \sum S -x$ et donc $x=B$.  Ceci montre que $S'$ amputé de cet entier supplémentaire est une solution au problème de Subset Sum.

L'autre direction de la preuve est similaire.


## Load Balancing

Considérons seulement m=2 machines. Soit $B=\sum p_i / 2$. Alors il existe une solution de valeur $B$ si et seulement l'instance $\langle p_1,\ldots,p_n,B\rangle$ au problème de 2-Partition a une solution.

## Hamiltonian cycle

Pour un sommet $u$ fixé, reliez les sorties et entrées des gadgets correspondant aux arêtes adjacentes à $u$ en une chaine.

Ajoutez k sommets. Reliez la sortie des chaines vers ces sommets et reliez ces sommets vers les entrées des chaines.


## Règle de chantier

Soit $a_1,\ldots,a_n$ une instance à 2-Partition. Soit B suffisamment grand et pair, disons $8n + 2a_1 + \ldots + 2a_n$.
On définit une instance au problème de la règle de chantier 
par la séquence des longueurs $B, B/2, 2+a_1, \ldots, 2+a_n, B/2, B$.
Ainsi la partie des $n$ segments du centre doit se plier pour que le départ et l'arrivée soient à la même position $B/2$.

