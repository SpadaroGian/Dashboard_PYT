# Dashboard APP : A look into the world's population

Ce dépôt de code contient le code pour une application de tableau de bord interactif construite avec Dash, Plotly et Python. 
L'application permet aux utilisateurs de visualiser et d'explorer les données de population et de revenus pour différents pays.

## Table of Contents

- [User Guide](#User Guide)
- [Aperçu](#Aperçu)
- [Developper Guide](#Developper Guide)
- [Rapport d analyse](#Rapport d analyse)


## User Guide

- Ouvrez votre terminal ou votre invite de commande.
- Utilisez la commande suivante pour cloner le dépôt : git clone <URL_du_dépôt>
- Naviguez jusqu'au répertoire du dépôt cloné en utilisant la commande cd.
- Une fois à l'intérieur du répertoire du dépôt, exécutez la commande suivante : -m pip install -r requirements.txt
- Assurez-vous d'avoir Python et Git installés sur votre système pour exécuter ces commandes
- Le dashboard sera lancé avec la commande: $ python main.py

## Aperçu

L'application se compose de plusieurs fichiers :

- **`requirements.txt`**: facilite le téléchargement des extensions nécessaires pour notre projet.
- **`main.py`**: Le point d'entrée de notre projet.
- **`data_fetch.py`**: Facilite la récupération des données depuis l'API.
- **`dashboard_layout.py`**: Désigne la mise en page. Cela inclut la manière dont les différents éléments, graphiques, et informations sont organisés et présentés sur notre application.
- **`callbacks.py`**: Définit des fonctions utilisées pour mettre à jour les graphiques interactifs dans notre application.

## Developper Guide :

### `main.py`

Ce module Python configure et lance une application de tableau de bord interactif utilisant Dash pour la visualisation des données de population et de niveaux de revenus provenant de l'API de la Banque mondiale.

### `dashboard_layout.py`

Ce fichier crée une mise en page divisée en différentes sections, chacune avec des éléments interactifs , pour explorer et visualiser des données sur la population mondiale et les niveaux de revenu. 
- `create_layout` : utilisée pour définir la structure de la page web. Les styles CSS sont utilisés pour définir l'apparence de ces éléments.

### `data_fetch.py`

Le module `Data_fetch.py` permet de récupérer des données à partir de l'API de la Banque mondiale, les transformer en structures de données utilisables (DataFrames) 
à l'aide de pandas, et encapsuler ces opérations dans des fonctions distinctes pour la réutilisation et la clarté du code.

- `fetch_data` : Permet de récupérer les données de population de tous les pays à partir de l'API de la Banque mondiale.
- `fetch_data2` : Permet de récupérer les données économiques de tous les pays à partir de l'API de la Banque mondiale.

Ces deux fonctions sont conçues pour effectuer des requêtes à l'API, collecter les données pertinentes, 
puis les transformer en DataFrames pandas pour une utilisation ultérieure dans l'application ou d'autres opérations d'analyse de données.

### `callbacks.py`

Le module `callbacks.py` inclut des fonctions pour mettre à jour différents graphiques en fonction des sélections de l'utilisateur :

- `update_graph` : Met à jour un graphique en ligne montrant les tendances de la population pour les pays sélectionnés.
- `update_histogram` : Génère un histogramme affichant les distributions de population pour les pays choisis.
- `update_map` : Construit une carte choroplèthe montrant les données de population pour les pays sélectionnés pour une année spécifique.
- `update_income_graph` : Rafraîchit un graphique de dispersion montrant les disparités de revenus entre les pays choisis.

Les callbacks sont liés à des éléments d'interface utilisateur spécifiques (par exemple, les menus déroulants) dans l'application Dash pour mettre à jour dynamiquement les visualisations en fonction des entrées de l'utilisateur.

## Rapport d analyse :

Exploitation des données dynamiques pour élaborer une analyse sur la corrélation entre la population et le revenu dans divers pays.

Parmi les pays sélectionnés, on peut trouver la France, le Brésil et le Burkina Faso. Nous avons choisi ces trois pays car ils présentent des niveaux de revenu totalement différents.

En France, avec une population relativement stable, l'accent pourrait être mis sur la répartition des revenus. Le niveau moyen/élevé de revenu indique une certaine stabilité économique et peut refléter des politiques sociales solides.

Vieillissement de la population et impact sur l'économie : Bien que nos données ne couvrent pas directement le vieillissement démographique, nous soulignerons comment cela pourrait influer sur les modèles de consommation, les dépenses de santé et les retraites, impactant potentiellement la croissance économique à long terme.

Au Burkina Faso, la population est en croissance, le revenu est plus faible : Une population en croissance avec des revenus généralement inférieurs pourrait souligner les défis économiques et sociaux auxquels le pays est confronté. Cela peut indiquer des besoins accrus en matière d'éducation, d'emploi et de services sociaux pour soutenir une population en expansion.

Relations générales entre la population et l'économie :

Impact sur la consommation et la production : Dans tous les pays, une population plus importante pourrait être associée à une demande de biens et de services plus importante, stimulant potentiellement la production économique. Cependant, cela dépend fortement du niveau de revenu et de la répartition de celui-ci au sein de la population.

Investissement dans le capital humain : Les données sur la population et le revenu pourraient souligner l'importance des investissements dans le capital humain (éducation, santé, formation) pour favoriser une économie plus productive et inclusive.

