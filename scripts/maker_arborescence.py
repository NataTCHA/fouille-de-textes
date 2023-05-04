import os
import argparse

argParser = argparse.ArgumentParser()

# Création argument obligatoire : nom du fichier XML à traiter
argParser.add_argument('filename', help="fichier TXT à traiter sans l'extension !")
args = argParser.parse_args()

fichier_traite = args.filename+'.txt'


#_________________________________________________________________________________

#Vérification de l'existence d'un dossier pour la classe sinon il est créé
directory = args.filename
base_dir="corpus"

path = os.path.join(base_dir, directory)

isExist = os.path.exists(base_dir)
if not isExist:
   os.makedirs(base_dir)
   print(f"Création du dossier {base_dir} réussie.")
   
isExist = os.path.exists(path)
if not isExist:
   os.makedirs(path)
   print(f"Création du dossier {path} réussie.")

#_________________________________________________________________________________


def split_file(filename, lines_per_file):
    '''fonction permettant de créer un dossier pour la classe spécifiées et des fichiers texte contenant 10 lignes (10 appréciations) à partir du fichier texte contenant toutes les appréciations de la classe spécifiée'''
    with open(filename, "r") as input_file:
        # Initialise le compteur de lignes et le numéro de séquence de fichier
        line_count = 0
        file_seq = 1
        # Initialise le fichier de sortie
        output_filename = args.filename + "_{:02d}.txt".format(file_seq)
        output_file = open(f"{path}/{output_filename}", "w")
        for line in input_file:
            output_file.write(line)
            line_count += 1

            if line_count >= lines_per_file:
                output_file.close()

                file_seq += 1

                output_filename = args.filename + "_{:02d}.txt".format(file_seq)
                output_file = open(f"{path}/{output_filename}", "w")

                line_count = 0

        output_file.close()

split_file(fichier_traite, 10)
