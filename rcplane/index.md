---
title: Mon abécédaire de l'aéromodélisme
lang: fr-FR
---

    The Wright Bothers weren't the first to fly. They were just the first not to crash.

## Armin Wing

Une construction d'aile en depron, décrite par Ed de [Experimental Airlines](https://www.youtube.com/watch?v=karr67ZYho4) et puis par [Andrew Newton](http://newtonairlines.blogspot.com/2014/05/better-airfoil-wing-build.html).  Très simple à mettre en œuvre.

## Canaux

Voici l'association des canaux aux moteurs servos que j'utilise habituellement.
Écrire AETR ou AETRA près du récepteur pour mémoriser l'ordre de connexion (le premier A en rouge, le dernier en vert). Également marquer les câbles pour les servos ailerons avec des couleurs rouge (gauche) et vert (droite).

1. left aileron
2. elevator
3. throttle
4. rudder
5. right aileron

## Clubs

- [Les Goélands à Montreuil](http://goelmodaero.wixsite.com/goelmod/rc-exterieure)
- [Queue en brie](https://www.google.com/maps/@48.7742232,2.5729774,157m/data=!3m1!1e3?hl=en), notre terrain officiel avec piste

## Cockpits

- [jolie collection de photos](http://www.laboiteverte.fr/21-cockpits-davions/)

## Construction maison

En anglais: *scratch build*.
Plusieurs sites web ou canaux vidéos que je j'aime.

- [FliteTest](https://www.flitetest.com/) des vidéos très professionnels, avec des américains qui se la pêtent un peu, et vendent leur kits de fabrication.  Ils font tout avec du Dollar Tree Foam  et de la colle chaude. Fabrication rapide.
C'est difficile de trouver du matériel équivalent en France.
- [Experimental Airlines](https://www.youtube.com/user/ExperimentalAirlines) : un autre américain, apprend bien comment faire des ailes, recouvrir de ruban adhésif la surface.  Des constructions simples et robustes. A arrêté ce loisir depuis quelques années.
- [Andrew Newton](http://newtonairlines.blogspot.com/) un australien, qui a la chance d'aller voler facilement au bord d'une pente au bord de la mer.  Beaucoup de comparaison de matériels.
- [Erwin Beizeiten](https://www.youtube.com/channel/UCjSQBeTUKgqESVG9P7XJhmg) un autrichien qui construit dans un atelier tout rangé.
- [Papy Kilowatt](http://papykilowatt.free.fr/) un français qui avait atteint un niveau de précision et de réalisme incroyable.
- [Jivaro models](http://www.jivaro-models.org/) une collection française d'avions de toutes sortes.
- [Paul K. Johnson, seulement balsa](http://www.airfieldmodels.com/information_source/how_to_articles_for_model_builders/index.htm)

## Deviation

C'est le logiciel qui tourne sur ma radio commande, [Jumper T8SG](https://www.banggood.com/Jumper-T8SG-V2_0-Plus-Hall-Gimbal-Multi-protocol-Advanced-2_7-OLED-Transmitter-for-Flysky-Frsky-p-1257102.html).  J'ai choisi cette radio commande pour pouvoir parler à des récepteurs de plusieurs marques.  Avec un peu de bricolage on peut la faire [parler](https://www.deviationtx.com/wiki/voiceoutput). Gadget? En tout cas on a un retour des commandes sans perdre des yeux son avion.  

Voici comment j'ai configuré le logiciel de l'émetteur Jumper.
D'abord pour mettre un minuteur proportionnel à la commande moteur, je dois créer un canal virtuel, appelé disons "gaz100".  L'idée est de traduire l'entrée *Throttle* qui varie de -100 à +100 vers un canal variant entre 0 et +100.

~~~
[virtchan1]
name=gaz100
template=simple
[mixer]
src=THR
dest=Virt1
scalar=50
offset=50
curvetype=expo
points=0,0
~~~

Puis je programme deux minuteurs, les deux commandés par l'interrupteur H. Le premier compte juste le temps de vol. Le deuxième est un compte à rebours, qui diminue proportionnelement au canal Virt1.

~~~
[timer1]
src=SW H1
resetsrc=SW H0
[timer2]
type=cntdn-prop
src=Virt1
resetsrc=SW H0
time=360
~~~

Pour les ailerons j'ai programmé les canaux 1 et 5, pour l'aileron gauche et droite. Sur l'interrupteur C2 je les mets tous les deux en position haute maximale, ce qui est la position de l'aérofrein.  Avec mon règlage les ailerons débattent de +/- 1 centimètre et l'aérofrein monte à +3cm.

~~~
[channel1]
template=complex
[mixer]
src=AIL
dest=Ch1
scalar=60
[mixer]
src=AIL
dest=Ch1
switch=SW C2
scalar=-125
curvetype=fixed

[channel5]
template=complex
[mixer]
src=AIL
dest=Ch5
scalar=60
[mixer]
src=AIL
dest=Ch5
switch=SW C2
curvetype=fixed
~~~

## Drones

- [acrobatique et sportif](https://www.youtube.com/watch?v=Iz42lvAVbiI)

## Élastique

Voici des avions propulsés par un moteur avec élastique.

- [depron et bambou](https://www.youtube.com/watch?v=IIxm27JYnOI&list=PLRvRak4_g1MFiVh4VyPWio8DHTZhcE5xQ&index=11&t=0s)
- [bambou et sac nylon](https://www.youtube.com/watch?v=MzL8wztyVMU&list=PLRvRak4_g1MFiVh4VyPWio8DHTZhcE5xQ&index=12&t=0s)

## Empannage

Il s'agit de la queue de l'avion avec la dérive et la profondeur. C'est une pièce délicate à transporter d'autant plus qu'elle doit être super legère. Chaque gramme de plus dans l'empennage nécessite peut être 3 grammes de plus dans le nez.  [Voici](https://mikaeromodelisme.wordpress.com/2013/08/31/empennage-papillon-demontable/) une jolie méthode pour rendre le tout démontable.

## polystyrène expansé

Des gros blocs d'isolants, souvent rose, ou blanc cassé ou bleu clair.  Existe en plusieurs densités. Se découpe facile au fil chaud.  Il faut le poncer pour pouvoir coller sur la surface. Si du ruban adhésif n'adhère pas, on peut passer d'abord une fine couche de colle universelle diluée pour lisser la surface.

![(C) thyzoon](http://www.thyzoon.fr/Aeromod/Fil_chaud/img/fil_chaud_1.jpg)

## polypropylène expansé, ou EPP

C'est une mousse, à la surface lisse.  On peut la tordre en la chauffant avec un décapeur, puis la plier sur un tube ou un coin de table arrondi. Il parait que de la vapeur d'eau ou un sèche cheveux peut aussi faire l'affaire, mais je n'ai pas réussi, pas assez chaud.  Ou alors coller un film ou ruban adhésif sur une face pour prendre la tension, puis la plier sans qu'elle se brise.  De toute façon recouvrir cette mousse permet de la rendre plus solide. Par exemple avec un ruban adhésif coloré, comme ceux vendus par exemple chez Leroy Merlin pour les déménagements (une couleur par chambre). Sinon voir la section Marouflage.

![(C) Jivaro models](http://www.jivaro-models.org/p47_thunderbolt/012s.jpg)

|nom                                            |densité     |
|-----------------------------------------------|------------|
| dollar tree foam board                        | 297 g/m^2  |
|rogier et plé, mouse recouvert de papier kraft | 414 g/m^2  |
| [Depron](https://www.leroymerlin.fr/v3/p/produits/carton-de-20-plaques-mur-depron-l-1000-x-l-1000-x-ep-3-mm-e1400774731) 6mm, Leroy merlin par exemple          | 198 g/m^2  |

## polypropylène extrudé

C'est une mousse avec de grosses bulles.  Elle est pratiquement incassable.  Un nez d'avion dans ce matériel est idéal pour absorber les chocs. Difficile de traiter la surface, comme elle n'est pas lisse, les rubans adhésifs n'adhèrent pas. Un peu trop flexible pour fabriquer le reste de l'avion avec cette mousse.

![(C) Sapronit](https://www.sapronit.com/system/image_de_galeries/fichiers/000/000/342/vignette/Fabricant-Plaques-Mousse-PE-Multilam.JPG?1442929493)

## F3K

Dans ce loisir il y a des compétitions, avec beaucoup de catégories. Donc on en trouve forcément une où on peut gagner des médailles. Mais ce qui m'attire ce sont les avions de la catégorie F3k. Des planeurs sans hélice qu'on lance à la main par le saumon. C'est beau. Et super technique pour fabriquer un avion de haute performance.

- [Jan Henning](https://www.youtube.com/watch?v=p5BsfmUrtDM&list=PLZdOy4nGe2QKGPChQ_nEaEKesgN3__jY1)

## Marouflage

- Papy Kilowatt a expliqué [ici](http://papykilowatt.free.fr/html/page_trucs.htm) comment il maroufle avec du papier ses avions.
- [voici](https://www.flitetest.com/articles/super-strong-waterproof-foam-core) une étude comparative sur la solidité et prix de plusieurs méthodes pour créer une surface sandwich avec un cœur depron.  En gros, un marouflage avec du papier Kraft n'a pas de très bonnes caractéristiques contre deux couches de fibre de verre avec de la résine epoxy, qui elle n'est pas si chère que ça. Mais le choix de la colle utilisée est très important ici.


## Mes avions

- [MinimumRC CJ-6](https://fr.aliexpress.com/item/32826439827.html) --- Ma première construction. L'électronique est difficile à acheter, en tout cas à un prix raisonnable.  Leçon d'un premier vol : il faut absolument des ailerons pour une aile basse, sinon ce n'est pas stable.
- [Nutball](nutball) --- n'existe plus. Mais super simple à fabriquer et pas si facile à voler.
- [Simple CUB](https://www.flitetest.com/articles/diy-ft-simple-cub-build) --- jolie forme, mais le mien est devenu beaucoup trop lourd, et donc je le trouve difficile à voler. Aussi il prend beaucoup le vent et a besoin d'une météo calme.  J'aime bien le concept *swappable* de Flite Test. On met ESC, récepteur et moteur sur un tiroir, qu'on peut déplacer de modèle en modèle.
- Notre [version](a_newton_pusher) d'un planeur de Andrew Newton.  Je trouve qu'il est parfait pour débuter, car il peut encaisser un atterrissage sur le nez, et si on est en difficulté on peut simplement couper le moteur et le laisser planer.
- [Le planeur libellule](libellule)
- Planeur Savattero 60 --- première création personnelle, inspiré de ce [planeur](https://www.flitetest.com/articles/cheap-simple-foam-dlg-with-good-performance) --- Je l'ai fait car j'avais des composantes électroniques à réutiliser (à 10 Euros le moteur servo il ne faut les laisser dans un tiroir) et qu'on ne peut y plus connecter un moteur.  Je trouve que l'aile n'a pas assez de dièdre.
- [Planeur LIDL](LIDL-pitcherons) avec des ailes à incidence intégrale. Intéressant à voler.

Certaines photos sont [ici](https://photos.app.goo.gl/TNx8DpYNiykMsnXA6).

## Modèles

Les modèles que j'aime bien, et que j'aimerais fabriquer.

- [Piper Cherokee](http://paper-replika.com/index.php?option=com_content&view=article&id=9597:piper-cherokee-rc-plane&catid=144:rc-projects&Itemid=207908) par [Julius Perdana](https://www.youtube.com/channel/UC64lnLfKm09f13iayaCOX0A), un Indonésien très doué et sympathique.
- [Micro Skyhunter](http://newtonairlines.blogspot.com/search/label/-%20Micro%20Skyhunter) un petit avion bien pour le vol en immersion.  Peut-être il serait bien avec un empannage en A.
- [Pyth 700](http://www.jivaro-models.org/pyth700/page_pyth_700.html) une aile volante pour l'adrénaline. Facile à fabriquer et très solide.
- [Piper 120cm en Balsa](https://fr.aliexpress.com/item/32823979442.html)


## Monde

[Allemagne](https://www.youtube.com/watch?v=5IoODRH1TWg),
[Algérie](https://www.youtube.com/watch?v=pkT6ph5hnI0),
[Cambodge?](https://www.youtube.com/watch?v=VTY1XNBB7Zw&list=PLRvRak4_g1MFiVh4VyPWio8DHTZhcE5xQ&index=7&t=0s),
[Chili](https://www.youtube.com/watch?v=uR6z-mhI2Rw),
[Corée](https://www.youtube.com/watch?v=BXKDoljaN5M&list=PLRvRak4_g1MFiVh4VyPWio8DHTZhcE5xQ&index=2&t=0s),
[France, Dune du Pyla](https://www.youtube.com/watch?v=LvHpH7abGMw),
[France, Île d'Oléron](https://www.youtube.com/watch?v=YOiyY4KO8Ko),
[Inde (Bengal)](https://www.youtube.com/watch?v=phg_-ze8iuE&list=PLRvRak4_g1MFiVh4VyPWio8DHTZhcE5xQ&index=10&t=0s),
[Inde, dans les arrières cours](https://www.youtube.com/watch?v=LU1qoYxjeyw&list=PLRvRak4_g1MFiVh4VyPWio8DHTZhcE5xQ&index=6&t=0s),
[Japon](https://www.youtube.com/watch?v=JmRkxZT4XhY),
[Malaisie](https://www.youtube.com/watch?v=3lq_Rbq6jxo&list=PLRvRak4_g1MFiVh4VyPWio8DHTZhcE5xQ&index=9&t=0s),
[Maroc](https://www.youtube.com/watch?v=EZlvMI35p5I&t=5s),
[Suisse](https://www.youtube.com/watch?v=xa-jmbQRw_8),
[Thailand](https://www.youtube.com/watch?v=148qPteAXQ0),
[Vietnam](https://www.youtube.com/watch?v=nDO9c2nMylU).

## Papier

[The paper airplane guy](https://www.youtube.com/watch?v=3BNg4fDJC8A&list=PLRvRak4_g1MFiVh4VyPWio8DHTZhcE5xQ&index=4&t=384s)

## Pitcheron

Aussi appelé *ailes à incidence intégrale*.
Quand les ailes entiers tournent autour d'un axe, gauche et droite indépendamment. Permet de simuler la profondeur et les ailerons.
Sur la radio commande faire les mêmes réglages comme pour une aile volante je pense.

D'après [Kyle Clayton](https://www.rcgroups.com/forums/showthread.php?1133158-How-to-set-up-a-pitcheron):

- To go down, the leading edge (LE) of both wings goes down
- To bank right, right wing LE goes down, left LE goes up
- To bank left, vice versa of above

## Sandow

Propulser un planeur par treuil élastique, c'est expliqué en [français](http://www.aeromod.eu/Catapulte_fra.htm) et en [anglais](https://www.instructables.com/id/Greenest-Way-to-Fly-RC/).

## Simulateur

J'ai juste de l'expérience avec Phoenix. J'aime bien le fait qu'on puisse régler la force et régularité du vent, c'est une bonne préparation.  
Nécessite une manette connecté en USB. N'a pas fonctionné avec l'émetteur Jumper T8SG. J'ai utilisé [cette](https://www.banggood.com/Wholesale-Httpwww_banggood_comWholesale-6CH-G4-XTR5_0-RC-Remote-Control-Flight-Simulator-For-Helicopter-Airplane-p-55419_html-p-55419.html?rmmds=myorder&cur_warehouse=CN) manette dédiée à la simulation, qui fonctionne très bien (mais coûtait beaucoup moins, de l'ordre de 15€, au moment de l'achat que maintenant).

La plupart des simulateurs sont très chers. PicaSim est gratuit, mais je n'ai pas encore réussit à l'utiliser.  [RC Desk Pilot](https://github.com/davyloots/rcdeskpilot) est un autre projet sous licence GNU.  Je n'ai pas trouvé d'exécutable à télécharger, mais on peut le compiler.

On peut connecter son émetteur via le port d'écolage à l'entrée audio de l'ordinateur et utiliser le programme [SmartPropoPlus] pour émuler un Joystick.  Ceci ne fonctionne pas avec Phoenix.

J'ai fini par trouver une solution, qui me permet de commander le simulateur Phoenix avec la radio commande Jumper. C'est ce [dongle](https://www.aliexpress.com/item/22-in-1-RC-USB-Flight-Simulator-with-Cables-for-Realflight-G7-G6-G5-Aero-Fly/32835905606.html) qui se branche sur la sortie PPM avec le câble audio fourni.  Il faut alors créer un modèle au protocole PPM.

On peut lire que la Jumper permet de fonctionner comme un joystick sous Windows via le câble USB, avec un modèle via le protocole USBHID.  Mais je n'ai pas réussit à la faire fonctionner ainsi, avec différents simulateurs.


## Terrains

Le site [geoportail](https://www.geoportail.gouv.fr/) montre où est-ce qu'on peut officiellement voler.

## Volets

En anglais : *flaps*. Servent à augmenter la portance de l'aile et à atterrir et décoller avec des vitesses plus faibles. Pas nécessaire pour des petits avions.

- [la Rolls Royce des volets](https://www.youtube.com/watch?v=_VjWMka-bxQ)
