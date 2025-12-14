# Gestion de Flotte Spatiale — Projet Python

Ce programme permet de gérer une flotte de vaisseaux spatiaux via un menu interactif en terminal. Il simule des opérations de gestion, d’équipage et d’événements aléatoires dans un univers spatial.

---

## Fonctionnalités principales

- **Renommer la flotte** avec confirmation et sauvegarde.
- **Ajouter ou supprimer des vaisseaux** avec validation stricte.
- **Gérer l’équipage** : ajout et suppression de membres (opérateurs ou mentalistes).
- **Afficher les informations d’un équipage** avec détails complets.
- **Vérifier la préparation d’un vaisseau** avant le départ.
- **Sauvegarder la flotte** dans un fichier JSON.
- **Afficher les statistiques globales** de la flotte.
- **Déclencher un événement aléatoire** (attaque ou renfort), appliqué et sauvegardé automatiquement.
- **Quitter le programme** proprement.

---

## Structure du projet

- `main.py` : point d’entrée du programme avec le menu principal.
- `Fleet.py` : classe principale représentant la flotte.
- `Spaceship.py` : classe pour chaque vaisseau.
- `Operator.py` : classe pour les membres d’équipage de type opérateur.
- `Mentalist.py` : classe pour les membres d’équipage de type mentaliste.
- `Member.py` : classe de base pour tout membre d’équipage.
- `save_and_load_data.py` : fonctions de sauvegarde/chargement JSON.
- `data.json` : fichier de persistance des données.

---

## Classes principales

### `Fleet`
- Représente une flotte entière.
- Attributs : nom de la flotte, liste de vaisseaux.
- Méthodes : `append_spaceship()`, `remove_spaceship()`, `get_spaceships()`, `set_name()`, etc.

### `Spaceship`
- Représente un vaisseau individuel.
- Attributs : nom, type (marchand, guerre, transport), état (`condition`), équipage.
- Méthodes : `append_member()`, `remove_member()`, `get_crew()`, `check_preparation()`.

### `Member`
- Classe de base pour tout membre d’équipage.
- Attributs : prénom, nom, genre, âge.
- Méthodes : getters pour accéder aux informations.

### `Operator` (hérite de `Member`)
- Spécialisation pour les opérateurs.
- Attributs supplémentaires : rôle (pilote, technicien, commandant), expérience.
- Méthodes : gestion de l’expérience.

### `Mentalist` (hérite de `Member`)
- Spécialisation pour les mentalistes.
- Attributs supplémentaires : mana.
- Méthodes : gestion des pouvoirs mentaux.

---

## Bonus implémentés

-  Logique stricte de confirmation avant toute modification.
-  Événements aléatoires avec sauvegarde automatique.
-  Affichage dynamique des équipages selon leur rôle.
-  Utilisation de setters/getters pour éviter l’accès direct aux attributs privés.

---
