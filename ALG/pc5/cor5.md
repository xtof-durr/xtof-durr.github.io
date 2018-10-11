---
title: Corrigé
---

École Centrale-Supélec - parcours Informatique et Systèmes Avancés - [Tronc commun](http://www.isia.ecp.fr/welcome_to_www_ecp_fr_cms_site_isia/isia___formation/cours_tronc_commun) - cours IS3005AD: Algorithmique Avancée

## Mission Improbable

D'abord on observe que si on peut diminuer la hauteur d'une pile, alors on peut la diminuer à $1$. 
Cherchons à déterminer les cases dont on peut diminuer la pile. Pour fixer la notation appelons \emph{hauteur} d'une ligne ou colonne la hauteur maximale de ses cases.

Considérons une pile de hauteur $h>1$ à l'intersection d'une ligne et d'une colonne de valeur strictement plus grande que $h$. Alors on peut diminuer tranquillement cette pile à hauteur $1$, car il y aura d'autres piles dans la même ligne et même colonne qui seront plus hauts. 

Désormais fixons une hauteur $h > 1$ et considerons le graphe bi-partie dont les sommets sont les lignes d'une part, les colonnes d'autre part et il y a une arête pour chaque pile de hauteur exactement $h$.  Ignorons les sommets isolés dans ce graphe et marquons les sommets correspondant à des lignes ou colonnes de hauteur maximale exactement $h$.  Les sommets (non isolés) non marqués ont une valeur strictement plus grande que $h$.  Il faut trouver un ensemble minimal $S$ d'arêtes dans ce graphe qui couvrent tous les sommets marqués.  Ces arêtes correspondent à des piles que le voleur doit préserver pour ne pas se faire reperer par les caméras.  

Si une arête est entre deux sommets non-marqués, elle ne fera pas partie d'une solution optimale $S$, car elle ne peut pas servir à couvrir un sommet marqué.  Desormais considérons deux arêtes $(u,v)$ et $(u,v')$ avec $u,v$ marqué et $v'$ non-marqué.  Alors il existe une solution optimale sans l'arête $(u,v')$, car on pourrait toujours l'échanger avec l'arête $(u,v)$.  Ceci veut dire que pour tout sommet $u$ marqué dans ce graphe, s'il a au moins un voisin marqué également, alors on peut supprimer toutes les arêtes adjacentes à $u$ qui mênent vers des voisins non-marqués.

De même s'il existe un sommet marqué qui n'a que des voisins non-marqués, on peut choisir une arête adjacente arbitraire pour la solution optimale $S$.  Le résultat de ces règles, est le problème classique de couverture par arêtes dans un graphe bi-parti, car toutes les arêtes restants sont entre deux sommets marqués.  Notons que d'un  point de vue pratique il n'est pas nécessaire de construire un tel graphe pour chaque hauteur $h$, mais on peut contruire l'union de ces graphe et appeler une seule fois un algorithme pour trouver une couverture minimale par arête.

## Champs boueux

C'est un problème de couverture par sommets.  Considérez le graphe biparti suivant. Chaque segment maximal composé de cases adjacents boueuses, correspond à un emplacement potentiel de planche et génère un sommet.  Il y a donc des sommets correspondant aux segments horizontaux et des sommets correspondant aux segments horizontaux.  Par convention, les cases boueux isolées génèrent deux sommets.  Dans ce graphe il y aura une arête par case boueuse entre les sommets correspondant au segment vertical et horizontal dont l'intersection est cette case.  Le but est de trouver un ensemble minimal de sommets qui couvre toutes les arêtes.

Comme chaque arête d'un couplage doit avoir au moins une extrémité dans $S$, la taille du couplage maximal est une borne inférieure sur la taille minimale dans la couverture minimale.  Le théorème de Kőnig dit qu'il y a en fait égalité entre les valeurs optimales.

La preuve du théorème est constructive et donne un algorithme pour trouver une couverture minimale à partir d'un couplage maximal $M$ pour le graphe $G(U,V,E)$.  Soit $Z$ l'ensemble des sommets non couplés par $M$, et qui sont dans $U$.  Ajoutons dans $Z$ tous les sommets atteignables à partir de $Z$ par des chemins alternants.  On définit un ensemble
\\[
S = (U\backslash Z) \cup (V\cap Z).
\\]

La construction de $Z$ implique que pour chaque arête $(u,v)\in M$, si $v\in Z$ alors $u\in Z$ également.  Et si $u\in Z$, comme $u$ n'était pas initialement dans $Z$ avec les sommets libres de $U$, $u$ a été ajouté à $Z$ grâce à l'arête du couplage, donc $v\in Z$.

Ceci implique que pour chaque arête du couplage $(u,v)\in M$, soit chacune de ses extrémités est dans $Z$ soit aucune ne l'est. Donc toute arête du couplage a exactement une extrémité dans $S$, et  $|S|\geq |M|$.

Montrons que $S$ couvre toutes les arêtes du graphe.
Soit $(u,v)$ une arête du graphe. Si $u \not\in Z$, l'arête est couverte, alors supposons que $u \in Z$.  Si $(u,v)$ n'est pas une arête du couplage, alors le caractère maximal de $Z$ fait que $v$ doit aussi être dans $Z$, et est donc dans $S$.
Si $(u,v)$ est dans $M$, alors par l'observation précédente $v\in Z$, et donc $v\in S$. Ceci montre que $S$ est une couverture de sommets, ce qui implique que $|S|\leq |M|$, ainsi nous pouvons conclure que \\(|S|=|M|\\).


![](konig.png "Calcul d'une couverture minimale par sommets. D'abord un couplage maximum est calculé, dont les arêtes sont montrées par des traits épais.  L'ensemble $Z$ est composé des sommets non couplés dans $U$ (en gris foncé), complété par les sommets atteignable de $Z$ par des chemins alternants (en gris clair).  Finalement la solution produite est l'ensemble $S=(U\backslash Z) \cup (V\cap Z)$, donc chacun des sommets est montré avec une ombre."){:width="600"}

## Flot maximum à coût minimum

Ici on voulait que vous observiez qu'une solution arbitraire non-optimale peut être améliorée en trouvant un cycle orienté C de valeur négative. La valeur serait définie comme la somme des coûts des arcs le long de C, le coût étant pris positivement quand C est orienté comme le flot sur l'arc, et négativement quand C est orienté à l'opposé du flot sur l'arc.  On peut alors définir $\delta$ comme la plus petite valeur par laquelle on peut modifier le flot le long de C sans violer les contraintes de capacité.  Les contraintes de préservation de flot sont préservées et le coût du flot diminuera de $\delta$ multiplié par la valeur de C. Ainsi on peut avoir une approche similaire à l'algorithme de Ford et Fulkerson.





