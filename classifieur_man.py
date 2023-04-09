
# ****************************************************************************                              
#                                                                              
#    classifieur.py                                                            
#                                                                                
#    By: @juliette, @natacha                                           
#    Created: 2023/03/22 16:21:48 by @juliette
#                  
# ****************************************************************************


from colorama import init as colorama_init
from colorama import Fore
from colorama import Style
import argparse

# recup fichier à trier
argParser = argparse.ArgumentParser()
# Création argument obligatoire : nom du fichier XML à traiter pk XML ???
argParser.add_argument('filename', help="fichier texte à traiter")
args = argParser.parse_args()

fichier_traite = args.filename
# pour lignes dans fichier, trier dans fichier correspondant ou quitter ajout de "a" pour ajouter et pas ecraser
positif = open("positif.txt", "a")
negatif = open("negatif.txt", "a")
mitige = open("mitige.txt", "a")

class bcolors:
    HEADER = '\033[95m'

lignes_restantes = []
with open(fichier_traite, 'r') as fichier:
    for line in fichier:
        line = line.strip()
        if line == "":
            continue
        print(f"\n{bcolors.HEADER}{line}{bcolors.ENDC}")
        reponse = input("Quel sentiment renvoie l'appréciation ? ").strip().upper()
        while reponse not in ["N", "P", "M", "Q"]:
            reponse = input("Vous avez entré une lettre invalide. Veuillez réessayer.").strip().upper()
        if reponse == "N":
            negatif.write(f"{line}\n")
        elif reponse == "P":
            positif.write(f"{line}\n")
        elif reponse == "M":
            mitige.write(f"{line}\n")
        elif reponse == "Q":
            #ici j ai mis un append pour bien ajouter la ligne qu'on ne traitera pas maintenant après on ferme la boucle
            lignes_restantes.append(line.strip())
            break
    #ici on continue notre parcours et on ajoute toutes les lignes qui n'ont pas été traité dans la liste ligne restantes et en fait si elle traite pas les lignes precedentes
    # c'est psk le curseur dans le fichier s'arrete bien à la dernière ligne non traité donc quand tu repasses une boucle ça passe bien par la ligne non traité
    #psk on a pas réouvert le fichier tu comprends ?
    for line in fichier:
        lignes_restantes.append(line.strip())
#fermer fichier
positif.close()
negatif.close()
mitige.close()

#fonction qui nous permet d ecraser le fichier traiter en ecrivant dedans toutes les lignes restantes 
def sauvegarder_fichier(nom_fichier, contenu):
    with open(nom_fichier, 'w') as f:
        f.write(contenu)

#fermer fichier
sauvegarder_fichier(fichier_traite, "\n".join(lignes_restantes))

