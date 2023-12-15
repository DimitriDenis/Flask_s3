# Application de Chargement de Vidéos vers S3

Cette application Flask permet de charger des vidéos au format mp4 vers un bucket S3 sur AWS.

## Installation

1. Assurez-vous d'avoir Python installé sur votre machine. Si ce n'est pas le cas, vous pouvez le télécharger sur [le site officiel de Python](https://www.python.org/).

2. Clonez ce dépôt GitHub sur votre machine locale :

    ```bash
    git clone https://github.com/votre-utilisateur/votre-repo.git
    ```

3. Accédez au répertoire de l'application :

    ```bash
    cd votre-repo
    ```

4. Installez les dépendances requises à l'aide de pip (il est recommandé d'utiliser un environnement virtuel) :

    ```bash
    pip install Flask Flask-Cors boto3 Werkzeug
    ```

## Configuration

1. Obtenez vos clés d'accès AWS (AWS Access Key ID et AWS Secret Access Key) et remplacez les valeurs correspondantes dans le fichier `app.py` :

    ```python
    aws_access_key_id='VOTRE_ACCESS_KEY_ID',
    aws_secret_access_key='VOTRE_SECRET_ACCESS_KEY'
    ```

2. Assurez-vous que votre bucket S3 est configuré correctement et remplacez le nom du bucket dans le fichier `app.py` :

    ```python
    bucket_name = 'NOM_DE_VOTRE_BUCKET'
    ```

## Utilisation

1. Lancez l'application Flask :

    ```bash
    python app.py
    ```

2. Accédez à l'application dans votre navigateur à l'adresse [http://localhost:5000/](http://localhost:5000/).

3. Téléchargez une vidéo au format mp4 en utilisant le formulaire d'upload.

4. Consultez la liste des vidéos téléchargées sur la page d'accueil.

## Note

Assurez-vous que votre bucket S3 est correctement configuré avec les autorisations nécessaires pour effectuer des opérations de lecture et d'écriture.

---

**Remarque :** Il est fortement recommandé de ne pas stocker vos clés d'accès AWS directement dans le code source pour des raisons de sécurité. Utilisez plutôt des variables d'environnement ou des méthodes de gestion de secrets.
