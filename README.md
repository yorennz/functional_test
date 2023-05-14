# Python Functional Test

Ce workshop vous permettra de vous familiariser avec les tests fonctionnels en Python en utilisant `pytest` ou `nose2`.
Que vous soyez en tek1 / tek2 / tek3 , n'oubliez pas que les tests meme en python sont acceptés en review sur vos projets en C / autre langage.

Testez son code ne s'arrete pas à les tester uniquement en C avec criterion ! Chacun son confort de test !

## Structure du Projet

Le projet comprend 4 modules principaux:

1. `exercice1.py` : Une simple classe de calculatrice avec des opérations de base.
2. `exercice2.py` : Une classe pour analyser les chaînes de caractères.
3. `exercice3.py` : Une classe de formes géométriques de base avec des sous-classes pour le rectangle, le carré et le cercle.
4. `exercice4.py` : Une classe pour gérer une base de données SQLite.


## MUST

Afin de se retrouver dans les memes situations qu'en projet, merci de fork le repo, créer un dossier `tests` et écrivez vos fichiers de tests dans le dossier avant de les lancer
Respectez la convention suivante pour chaque fichier de tests:
`test_exerciceX.py` avec X l'entier définissant l'exercice actuel.

## UTILS

Libre à vous de choisir le framework !
Pour ceux qui ont l'habitude de pytest, voila le bon moment pour essayer nose2 !

## Comment exécuter les tests

Pour exécuter les tests avec `pytest`, utilisez la commande suivante dans le dossier tests :

```bash
pytest --cov=../ test_exerciceX.py

