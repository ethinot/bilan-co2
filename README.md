
# C02 Tracker

## 🧐 À propos

Ce projet est proposé aux étudiant(e)s du Master 1 Informatique de l'Université Claude Bernard Lyon 1. À travers l'unité d'enseignement "Projet transversal" (M1if10)ce projet vise à développer les capacités de travail collaboratives, tout en mettant en pratique les connaissances acquises dans les autres UE du M1. 

Le sujet commun aux élèves de la promotion était de réaliser une application web proposant un service de calcul d'empreinte carbone.

## 🏁 C'est partie

Les instructions qui suivent vont vous permettrent des lancer le projet en local sur votre machine.

### Prérequis

- **Backend** : Python supérieure ou égale à 3.10
  - Créer un envirronnement virtuel Python (pas obligatoire mais plus propre)
    - `python3 -m venv chemin/vers/l/envirronnement`
  

-  **Frontend** :  Node.js version 18+. 20+

### Folder structure

<details>
<summary>Arborescence du projet</summary>

```
.
├── backend
│   ├── backend
│   │   └── __pycache__
│   ├── django_app
│   │   ├── __pycache__
│   │   └── migrations
│   │       └── __pycache__
│   ├── postman
│   └── static
│       ├── admin
│       │   ├── css
│       │   │   └── vendor
│       │   │       └── select2
│       │   ├── img
│       │   │   └── gis
│       │   └── js
│       │       ├── admin
│       │       └── vendor
│       │           ├── jquery
│       │           ├── select2
│       │           │   └── i18n
│       │           └── xregexp
│       └── rest_framework
│           ├── css
│           ├── docs
│           │   ├── css
│           │   ├── img
│           │   └── js
│           ├── fonts
│           ├── img
│           └── js
└── frontend
    ├── public
    └── src
        ├── api
        ├── assets
        ├── components
        │   ├── auth
        │   ├── dashboard
        │   │   └── sidebar
        │   ├── footer
        │   ├── navbar
        │   ├── save
        │   └── ui
        │       ├── avatar
        │       ├── button
        │       ├── card
        │       └── dropdown-menu
        ├── layouts
        ├── lib
        ├── pages
        │   ├── protected
        │   └── public
        ├── router
        ├── store
        └── validation

```

</details>

### Installation

- Ouvrir votre terminal à la racine du projet

- Installer les dépendances

    - pour le backend :
    `pip install -r requirement.txt `
      - si vous travaillez dans un environnement Python, penser à l'activer avant d'installer les dépendances : \
        `source chemin/vers/l/envirronnement/bin/activate`

    - pour le frontend :
    `cd frontend && npm install `

    

## 🎈 Utilisations

Après l'Installation des dépendances :

### Backend 
#### Configuration du fichier `.env`

1. Créez un fichier nommé `.env` dans le répertoire `backend/backend`.
2. Ajoutez-y les lignes suivantes :

```plaintext
SECRET_KEY=
DATABASE_USERNAME=
DATABASE_PASSWORD=
```

#### Génération de la clé secrète Django

1. Ouvrez un terminal à la racine du projet.
2. Exécutez la commande suivante pour générer une clé secrète Django :

```shell
python3 -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

3. Copiez la clé générée et collez-la dans le fichier `.env` que vous avez créé précédemment sous la variable `SECRET_KEY`.

#### Mise à jour de la base de données

Après avoir configuré le fichier `.env`, vous devez effectuer les migrations nécessaires pour mettre à jour votre base de données. Voici comment faire :

1. Assurez-vous d'être dans le répertoire `backend/backend` dans votre terminal.
2. Exécutez les commandes suivantes :

```shell
python3 manage.py makemigrations
python3 manage.py migrate
```

Ces commandes créeront les migrations nécessaires en fonction des modèles de votre application Django et les appliqueront à votre base de données.

Avec ces étapes supplémentaires, votre backend devrait être correctement configuré pour fonctionner avec votre projet.

#### Lancer l'application Django (backend)

```shell
cd backend/backend && python3 manage.py runserver
```

### Frontend
#### Lancer l'application Vue.js (frontend)

```shell
cd frontend && npm run dev
```

## ⛏️ Built Using

### Backend

- [Django](https://www.djangoproject.com/) : framework de création d'application web

### Frontend
- [Vite](https://vitejs.dev/) : Un outil de développement rapide pour la construction d'applications web modernes, Il se compose de deux parties principales :
  * **Un serveur de développement**.
  * **Une commande de construction** qui regroupe votre code avec [Rollup](https://rollupjs.org/), pré-configuré pour produire des ressources statiques hautement optimisées pour la production.
- [Vue.js](https://vuejs.org/) : Un framework JavaScript progressif pour la construction d'interfaces utilisateur dynamiques.



