---
title: Corrigé
---

École Centrale-Supélec - parcours Informatique et Systèmes Avancés - [Tronc commun](http://www.isia.ecp.fr/welcome_to_www_ecp_fr_cms_site_isia/isia___formation/cours_tronc_commun) - cours IS3005AD: Algorithmique Avancée

## Couverture par ensembles

1. Le coût d'un ensemble est réparti uniformément sur les éléments qu'il couvre et qui n'étaient pas encore couverts au moment de la sélection de l'ensemble. Appelons cette fraction *l'efficacité de coût*.  $c_u$ est la partie du coût qui revient à l'élément $u$.
2. Les deux sommes sont juste deux manières de compter le même coût.
3. Soit $R$ l'ensemble des éléments restant à couvrir au moment où $u_i$ s'appretait à être couvert. On a $|R|\geq n-i+1$. À tout moment les ensembles restants peuvent couvrir les éléments restants avec un coût total au plus OPT.  Un de ces ensembles doit avoir une efficacité de coût au plus OPT/|R|. Mais $u_i$ a été couvert par l'ensemble le plus efficace et donc 
\\[
		c_u \leq \frac{\textrm{OPT}}{|R|} \leq  \frac{\textrm{OPT}}{n-i+1}.
\\] 
4. On utilise le fait que le n-ème nombre harmonique satisfait $1+1/2+1/3+\ldots+1/n=O(\log n)$.

Voir [chapitre 2.1, Approximation Algorithms, Vijay V. Vazirani, Springer, 2001, traduction française 2006]

## Couverture par sommets

1. Associons chaque arête $e$ à une des ses extrémités dans $S$, avec un choix arbitraire si les deux sont dans $S$. Comme les prix sont équitables, pour tout sommet v dans S, la somme de $p_e$ sur les arêtes qui lui sont associées ne dépasse pas $w_v$.  Ceci montre l'inégalité demandée, déjà pour un sommet individuel dans S. En particulier $\sum_e p_e$ est une borne inférieure sur l'optimum OPT.
2. $w(S)=\sum_{v\in S} w_v = \sum_{v\in S} \sum_{e\ni v} p_e  \leq 2 \sum_{v\in V} \sum_{e\ni v} p_e =  2 \sum_e p_e$.
3. On combine $w(S) \leq 2 \sum_e p_e \leq 2\textrm{OPT}$.
