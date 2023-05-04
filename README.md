# Jounal de bord

## Groupe

Natacha M.
Juliette M.

## Sujet

Classification automatique d'appréciations scolaires en fonction du sentiment exprimé.

## Fonctionnement du Git
Dans le dossier appreciations nous retrouverons cette architecture :
* appreciations
    * positif.txt
    * mitigé.txt
    * negatif.txt

chaque fichier **.txt** contient le contenu totale de sa classe.  Ces trois fichiers textes ont permis de réaliser l'arborescence pour la mise en oeuvre du projet.

Ensuite nous avons le dossier corpus :
* corpus
    * positif
        * positif_[0-99].txt
    * mitige
        * mitige_[0-99].txt
    * negatif
        * negatif_[0-99].txt

Ce dossier est l'arborescence sur laquelle nous allons appliquer la vectorisation pour ensuite pouvoir travailler sur Weka. Celui ci a été conçu avec le script maker_arborescence.py

* scripts
  * classifieur_man.py
  * maker_arborescence.py
  * maker_bag_word.py

Le contenu de ce dossier est très important ! 
* **classifieur_man.py** nous a permis de constituer le dossier appréciations ou nous avons la totalité de nos appréciations triées en fonction de sa classe.
* **maker_bag_word.py** nous a permis de construire notre liste de mots vides ( nous avons tout de même dû y appliquer quelques correctifs manuels)
* **maker_arborescence.py** nous a permis de concevoir l'aborescence en lui donnant en entrée le dossier "appreciations". Il a écrit chaque fichier textuel : les fichiers ont 10 lignes textuelles.