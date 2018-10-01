---
title: Corrigé
---

École Centrale-Supélec - parcours Informatique et Systèmes Avancés - [Tronc commun](http://www.isia.ecp.fr/welcome_to_www_ecp_fr_cms_site_isia/isia___formation/cours_tronc_commun) - cours IS3005AD: Algorithmique Avancée

## Couplage bi-parti de cardinalité maximum

On augmente G par deux sommets source et destination. La source est reliée à tous les sommets de U, alors que la destination est reliée à tous les sommets de V. Toutes les arêtes ont la capacité 1. Maintenant il existe une bijection entre les flots dans ce graphe et les couplages dans le graphe initial.


## Élimination dans le baseball


Alors étant donnée \\(n\\) équipes, le nombre \\(w_i\\) de matchs déjà gagnés pour chaque équipe \\(i\\), et la liste des matchs \\((i,j)\\) encore à jouer on cherche à déterminer si une équipe particulière \\(k\\) a encore une chance de gagner.  


On va partir sur l'hypothèse la plus favorable pour l'équipe k, à savoir qu'elle gagnerait chacun de ses matchs. Soit a le nombre de match qu'elle a encore à jouer plus \\(w_k\\), le nombre de matchs déjà joués et gagnés par k.

On construit un graphe, composé d'une source s, d'un sommet (i,j) par match encore à jouer avec i,j différent de k, et d'un sommet i par équipe differente de k, ainsi que d'un sommet puits t. Il y a une arête de capacité 1 de la source à tous les sommets matchs. D'un sommet match (i,j) il y a une arête de capacité 1 à chacune des équipes i et j.  Dans un flot valide, une seule de ces arêtes serait utilisée et indiquerait l'équipe gagnante. Puis de chaque équipe i, il y a une arête vers le puits de capacité \\(a - w_i\\).  Cette capacité assure qu'aucune équipe n'arriverait à gagner plus de matchs que l'équipe k.  En particulier si une arête a une capacité négative, il n'y aura pas de solution.

## Entrepreneur cupide

Une solution S est de ratio au moins R, si 

\\[
	\frac{\sum_{i\in S} w_i}{\sum_{i\in S} p_i}  \leq R   
\\]
\\[
	\sum_{i\in S} w_i  \leq R  \sum_{i\in S} p_i 
\\]
\\[
	\sum_{i} w_i \leq \sum_{i\in S} R p_i + \sum_{i\not\in S} w_i
\\]

On veut faire correspondre des ensembles initiaux S avec des coupes dans le graphe.  Une coupe est un ensemble de sommets, on veut donc que les tâches correspondent à des sommets dans le graphe.
L'expression de la partie droite de l'inégalité contient des sommes sur les éléments de S, et donc il faudrait des arcs dans le graphe avec ces valeurs.  On peut aussi se servir d'arcs de capacité infinie, pour éviter de sélectionner des ensembles de sommets qui ne soient pas initiaux.

Notre graphe aura une source, un sommet par tâche et un puits. La source est reliée à chaque tâche i avec une capacité \\(w_i\\).
Chaque tache i est reliée au puits avec une capacité \\( R p_i \\). Pour chaque couple de tâches avec \\(i \prec j\\) il y a un arc de j à i avec capacité infinie.  Ces arcs ne feront jamais partie d'une coupe de valeur finie, et donc ces coupes correspondent à des ensembles initiaux.
Chaque coupe \\( S\cup\{\textrm{source}\} \\) est de valeur au moins \\(\sum_{i} w_i \\) ssi l'ensemble S est initial est a un ratio \\(\frac{\sum_{i\in S} w_i}{\sum_{i\in S} p_i} \\) au plus R.  Ainsi par recherche dichotomique sur R on peut trouver l'ensemble initial de plus grand ratio.
