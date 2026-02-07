# Elefan Boitier

Génération automatique de codes PIN pour les serrures intelligentes Igloo Home.

Cet utilitaire génère des codes PIN temporaires valables une semaine qui peuvent être utilisés pour déverrouiller les serrures intelligentes Igloo Home via l'API.

## Prérequis

- Python 3.8+
- Gestionnaire de paquets [uv](https://github.com/astral-sh/uv)

## Installation

1. **Clonez le dépôt** et naviguer vers le répertoire du projet :
   ```bash
   cd boitier
   ```

2. **Installez les dépendances** avec uv :
   ```bash
   uv sync
   ```

3. **Configurez les variables d'environnement** :
   
   Créez un fichier `.env` à la racine du projet avec vos identifiants API Igloo Home :
   ```
   IGLOO_HOME_CLIENT_ID=votre_client_id
   IGLOO_HOME_CLIENT_SECRET=votre_client_secret
   ```
   
   Ces identifiants sont disponibles dans le coffre-fort Keepass d'Elefan.

## Utilisation

Exécutez le script pour générer un code PIN :

```bash
uv run python elefan.py
```

Le script va :
1. S'authentifier auprès de l'API Igloo Home
2. Récupérer votre identifiant de périphérique
3. Générer un code PIN temporaire valable à partir de demain jusqu'à une semaine à partir de demain
4. Retourner le code PIN généré

Ensuite, copiez le code généré et enregistrez-le ici : https://membres.lelefan.org/codes/new

## Développement

Exécuter les tests :
```bash
uv run pytest
```

Formater et vérifier le code :
```bash
uv run ruff format .
uv run ruff check .
```

## Licence

MIT
