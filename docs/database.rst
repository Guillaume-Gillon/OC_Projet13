===============
Base de données
===============

La base de données utilisée est une base `SQLite <https://sqlite.org/index.html>`_.

* :ref:`Structure <structure_db>`
* :ref:`Modèles <models_db>`


.. _structure_db:

Structure
---------

La base de données contient les tables suivantes :

* *Profile* qui permet l'enregistrement des profils.
    __str__ : self.user.username
* *Address* qui permet de stocker les adresses de chaque biens.
    __str__ : f '{self.number} {self.street}'
* *Letting* qui permet d'enregistrer les biens disponibles.
    __str__ : self.title

| Les tables *Letting* et *Address* sont liées par un champ *OneToOne*.
| La table *Profile* est liée au modèle utilisateur de Django.

.. _models_db:

Modèles
-------

| Les modèles correspondent aux tables citées précédemment.
| Vous trouverez ci-dessous la description complète des champs.

**Profile** :

- *user* : Champ OneToOne lié au modèle utilisateur de Django.
    on_delete=models.CASCADE
- *favorite_city* : Champ texte (Charfield)
    max_length=64, blank=True

**Address** :

- *number* : Champ numérique (PositiveInteger)
    validators=[MaxValueValidator(9999)]
- *street* : Champ texte (Charfield)
    max_length=64
- *city* : Champ texte (Charfield)
    max_length=64
- *state* : Champ texte (Charfield)
    max_length=2, validators=[MinLengthValidator(2)]
- *zip_code* : Champ numérique (PositiveInteger)
    validators=[MaxValueValidator(9999)]
- *country_iso_code* : Champ texte (Charfield)
    max_length=3, validators=[MinLengthValidator(3)]

**Letting** :

- *title* : Champ texte (Charfield)
    max_length=256
- *address* : Champ OneToOne lié au modèle 'Address'
    on_delete=models.CASCADE