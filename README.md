#  Contexte

Ce défi porte sur le thème de la classification multimodale (texte et image) à grande échelle des codes de type de produit, dont l'objectif est de prédire le code de type de chaque produit tel que défini dans le catalogue de Rakuten France.

Le catalogage des fiches produits par catégorisation des titres et des images est un problème fondamental pour toute plateforme de commerce électronique, avec des applications allant de la recherche et des recommandations personnalisées à la compréhension des requêtes. Les approches manuelles et basées sur des règles de catégorisation ne sont pas évolutives, car les produits commerciaux sont organisés en de nombreuses catégories. Le déploiement d'approches multimodales serait une technique utile pour les entreprises de commerce électronique, car elles peinent à catégoriser les produits à partir des images et des étiquettes fournies par les marchands et à éviter les doublons, notamment lorsqu'elles vendent à la fois des produits neufs et d'occasion provenant de marchands professionnels et non professionnels, comme c'est le cas pour Rakuten. Les progrès dans ce domaine de recherche ont été limités par le manque de données réelles issues de catalogues commerciaux. Ce défi présente plusieurs pistes de recherche intéressantes en raison de la nature intrinsèquement imprécise des étiquettes et des images de produits, de la taille des catalogues de commerce électronique modernes et de la distribution généralement déséquilibrée des données.

#Description du problème

L’objectif de ce défi de données est la classification à grande échelle de données multimodales (texte et image) de produits en codes de type de produit .

Par exemple, dans le catalogue Rakuten France, un produit portant la désignation ou le titre français « Klarstein Présentoir 2 Montres Optique Fibre », associé à une image et parfois à une description, est classé sous le code de type de produit 1500. D'autres produits, avec des titres, des images et des descriptions différents, appartiennent au même code de type de produit. À partir de ces informations, comme dans l'exemple ci-dessus, ce défi propose de modéliser un classificateur permettant d'attribuer à chaque produit son code de type de produit correspondant.

#Métrique
La métrique utilisée dans ce défi pour classer les participants est le score F1 pondéré .

Le package Scikit-Learn dispose d'une implémentation de score F1 ( lien ) et peut être utilisé pour ce défi avec son averageparamètre défini sur "weighted".

#Description des données
Pour ce défi, Rakuten France met à disposition environ 99 000 fiches produits au format CSV, comprenant un ensemble d’entraînement (84 916) et un ensemble de test (13 812). L’ensemble de données contient les désignations, descriptions et images des produits, ainsi que leur code de type correspondant.

Les données sont divisées selon deux critères, formant quatre ensembles distincts : entraînement ou test, entrée ou sortie.

X_train.csv: fichier d'entrée d'entraînement
Y_train.csv: fichier de sortie d'entraînement
X_test.csv: fichier d'entrée de test
Un fichier contenant toutes les images est également images.zipfourni. Sa décompression créera un dossier nommé `training.jpg` imagescontenant deux sous-dossiers nommés ` training.jpg` image_traininget image_test`test.jpg`, contenant respectivement les images d'entraînement et de test.

La première ligne des fichiers d'entrée contient l'en-tête, et les colonnes sont séparées par une virgule ( ","). Les colonnes sont :

Un identifiant numérique pour le produit. Cet identifiant permet d'associer le produit à son code de type de produit correspondant.
Désignation - Le titre du produit, un court texte résumant le produit.
Description - Texte plus détaillé décrivant le produit. Ce champ n’est pas utilisé par tous les marchands ; par conséquent, afin de préserver l’originalité des données, le champ « Description » peut contenir la valeur NaN pour de nombreux produits .
productid - Un identifiant unique pour le produit.
imageid - Un identifiant unique pour l'image associée au produit.
Les champs imageid et productid permettent de récupérer les images depuis le dossier d'images correspondant. Pour un produit donné, le nom du fichier image estimage_imageid_product_productid.jpg : .

Voici un exemple de fichier d'entrée :

,designation,description,productid,imageid
0,Olivia: Personalisiertes Notizbuch 150 Seiten Punktraster Ca Din A5 Rosen-Design,,3804725264,1263597046
1,Journal Des Arts (Le) NÃ Â° 133 Du 28/09/2001 - L'art Et Son Marche Salon D'art Asiatique A Paris - Jacques Barrere - Francois Perrier - La Reforme Des Ventes Aux Encheres Publiques - Le Sna Fete Ses Cent Ans.,,436067568,1008141237

Le nom du fichier image correspondant au premier produit est image_1263597046_product_3804725264.jpg, et celui du second produit est image_1008141237_product_436067568.jpg. On peut rappeler que toutes les images correspondant aux produits d'entraînement listés dans X_train.csvse trouvent dans image_trainingle sous-dossier , et toutes les images correspondant aux produits de test listés dans X_test.csvse trouvent dans image_testle sous-dossier .

Le fichier de sortie d'entraînement ( Y_train.csv) contient prdtypecodela catégorie pour la tâche de classification, pour chaque identifiant entier dans le fichier d'entrée d'entraînement ( X_train.csv). Ici aussi, la première ligne du fichier est l'en-tête et les colonnes sont séparées par des virgules.

Voici un exemple du fichier de sortie :

,prdtypecode
0,10
1,2280

Pour le fichier d'entrée de test X_test.csv, les participants doivent fournir un fichier de sortie de test au même format que le fichier de sortie d'entraînement (en associant chaque identifiant numérique à la valeur prédite prdtypecode). La première ligne de ce fichier de sortie de test doit contenir l'en-tête ,prdtypecode.
