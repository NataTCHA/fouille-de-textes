# README

## Groupe :

Natacha M.
Juliette M.

## Sujet

Classification automatique d'appréciations scolaires en fonction du sentiment dégagé.

## Contenu du Git :

### Fichiers :

- **README.md** : c'est ça ! Il y a de tout, de l'explication de l'organisation du dossier à tout commentaire que nous avons jugé utile.
- **journal_de_bord.md** : notre journal de bord (assez synthétique parce que tout s'est globalement bien passé).

### Dossiers :

* <i>**appreciations/**
    * positif.txt
    * mitigé.txt
    * negatif.txt</i>
> Fichiers **.txt** contenant l'ensemble des appréciations du corpus, triées manuellement. C'est grâce à ces fichiers et au script <i>maker_arborescence.py</i> que nous avons pu créer notre arborescence finale.
___
* **corpus/**
    * positif/
        * positif_[01-66].txt
    * mitige/
        * mitige_[01-50].txt
    * negatif/
        * negatif_[01-50].txt
> Corpus de travail pour Weka. Chaque fichier texte fait 10 lignes (10 apréciations). Résulte de l'éxécution du script <i> maker_arborescence.py</i>.

___
* <i><b>scripts/</b>
  * classifieur_man.py
  * maker_arborescence.py
  * maker_bag_word.py</i>

>Dossier contenant les scripts python utilisés :
>-  **classifieur_man.py** : script qui prend en entrée le fichier <i>appreciations.txt</i> (fichier qui contenanit à la base l'ENSEMBLE des appréciations non triées) et qui, par un input de l'utilisateur, copie l'appréciation dans le fichier texte associé à sa classe. Les 3 fichiers de sortie sont ceux du dossier <i>appreciations</i>.
>- **maker_bag_word.py** : script qui mobilise NLTK pour traiter un fichier texte et créer un fichier mot vide associé. Le fichier de sortie est <i>motvide.txt</i>.
>- **maker_arborescence.py** nous a permis de concevoir l'aborescence du corpus pour Weka. Il se lance en ligne de commande et prend un argument qui correspond à la classe traité (positif, negatif, mitige). À partir du fichier texte contenant toutes les appréciations de la classe (<i>appreciations/</i>), il crée autant de fichier textuel de 10 lignes maximum qu'il peut y avoir.