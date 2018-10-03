---
title: Corrigé
---

École Centrale-Supélec - parcours Informatique et Systèmes Avancés - [Tronc commun](http://www.isia.ecp.fr/welcome_to_www_ecp_fr_cms_site_isia/isia___formation/cours_tronc_commun) - cours IS3005AD: Algorithmique Avancée

## Mission Improbable

D'abord on observe que si on peut diminuer la hauteur d'une pile, alors on peut la diminuer à $1$. 
Cherchons à déterminer les cases dont on peut diminuer la pile. Fixons une hauteur de pile $v$ et considérons toutes lignes $L$ et toutes les colonnes $C$ dont le maximum est $v$.  Si $L$ et $C$ sont vides, toutes les piles de hauteur $v$ peuvent être diminuées sans problème. Sinon, si seulement $C$ est vide par exemple, il suffit de garder exactement une pile de hauteur $v$ par ligne dans $L$, et le choix est sans importance.

Maintenant supposons que ni $L$ ni $C$ soient vides. Considéront les cases à l'intersection de ces lignes et colonnes.  Les cases de hauteur strictement inférieure à $v$ peuvent être diminuées sans problème. Mais parmi les cases de hauteur $v$ ont doit garder au moins une par ligne et au moins une par colonne. Notons que chaque hauteur $v$ distincte correspond à un sous-problème indépendant.

Il peut-être vu comme une variante du problème de couverture mentionné ci-haut. Considérons le graphe biparti où $L$ et $C$ sont les deux ensembles de sommets et il y a une arête entre le sommet $i\in L$ et le sommet $j\in C$, si la hauteur de la pile en $(i,j)$ est aussi $v$.  Le but est de trouver un ensemble minimal d'arêtes qui couvre tous les sommets.  Ces arêtes correspondent aux piles qui ne seront pas diminuées.  Un tel ensemble peut être trouvé en calculant un couplage maximal dans le graphe, qu'on complète pour chaque sommet $v$ non couplé par une arête arbitraire adjacente à $v$.
