
# C02 Tracker

## 🧐 À propos

**TODO**

## 🏁 C'est partie

Les instructions qui suivent vont vous permettrent des lancer le projet en local sur votre machine.

### Prérequis

- **TODO : tuto création du env python**

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

    - pour le frontend :
    `cd frontend && npm install `

    

## 🎈 Utilisations

Après l'Installation des dépendances :

- Lancer l'application Django (backend)

```shell
cd backend/backend && python3 manage.py runserver
```

- Lancer l'application Vue.js (frontend)

```shell
cd frontend && npm run dev
```

## ⛏️ Built Using

### Backend

- [Django](https://www.djangoproject.com/) : framework de création d'application web
- **TODO**

### Frontend
- [Vite](https://vitejs.dev/) : Un outil de développement rapide pour la construction d'applications web modernes, Il se compose de deux parties principales :
  * **Un serveur de développement**
  * **Une commande de construction** qui regroupe votre code avec [Rollup](https://rollupjs.org/), pré-configuré pour 
- [Vue.js](https://vuejs.org/) : Un framework JavaScript progressif pour la construction d'interfaces utilisateur dynamiques.



