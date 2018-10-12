---
title: Corrigé
---

École Centrale-Supélec - parcours Informatique et Systèmes Avancés - [Tronc commun](http://www.isia.ecp.fr/welcome_to_www_ecp_fr_cms_site_isia/isia___formation/cours_tronc_commun) - cours IS3005AD: Algorithmique Avancée

## Subset Sum

Soit $\langle G(V,E),k\rangle$ une instance de Vertex Cover.
On numérote les arêtes de $0$ à $m-1$ pour $m=|E|$, et les sommets $v_0, \ldots,v_{n-1}$ pour $n=|V|$.
Chaque sommet $v_j$ génère le nombre 
\\[
     a_j := 3^m + \sum_{v_j\in e_i} 3^i.
\\]
Soit $B = k \cdot 3^m + \sum_{i=0}^{m-1} 2 \cdot 3^i$.

Comme il n'y a pas de retenu dans les $m$ premiers chiffres, tout ensemble des $m$ nombres données et de valeur exactement $B$ correspond à une couverture par $k$ sommets et vice-versa.

## 2-Partition

On considère un problème de SUBSET-SUM, et on crée un ensemble $S'$ instance de 2-Partition en rajoutant un entier $a_{n+1}$ à $S$ de valeur $a_{n+1}=T-2V$ où $T$ est la somme totale des entiers de $S$. Si on trouve un solution à ce problème de 2-PARTITION, on retire $a_{n+1}$ du sous-ensemble renvoyé (où du complémentaire) et on obtient un sous-ensemble de $S$ de poids $\frac{T+T-2V}{2}-(T-2V)=V$. Si on a un solution de SUBSET-SUM on rajoute $a_{n+1}$ à ce sous-ensemble et on obtient un sous-ensemble de $S'$ de poids $V+T-2V= T-V$, le complémentaire de cet ensemble à un poids $T-V$.

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

