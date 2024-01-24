# Instructions d'Installation et d'Exécution

Pour installer les dépendances et exécuter l'application, suivez attentivement ces étapes :

## 1. Installation des Dépendances

Utilisez la commande suivante dans le terminal pour installer les dépendances à partir du fichier `requirements.txt` :

```bash
pip install -r requirements.txt
```

## 2. Installation du Modèle BERT

Avant de lancer l'application, assurez-vous d'avoir installé le modèle BERT pour l'encodage en exécutant le fichier `encoding.py`. Cela peut être fait avec la commande suivante :

```bash
python encoding.py
```

## 3. Configuration supplémentaire

Dans un fichier Python à côté de votre application, ajoutez les lignes de code suivantes pour garantir le bon fonctionnement de certaines bibliothèques :

```python
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
```

## 4. Lancement de l'Application

Enfin, pour exécuter l'application, utilisez la commande suivante dans le terminal en remplaçant `app.py` par le nom de votre fichier principal :

```bash
python app.py
```

Ces étapes garantissent une configuration correcte de l'environnement et permettent le bon fonctionnement de l'application. Vérifiez le fichier `readme.md` pour plus de détails sur l'utilisation et les fonctionnalités de votre application.
