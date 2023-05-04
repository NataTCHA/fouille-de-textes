import nltk
from nltk.corpus import stopwords

# Définition d'une fonction pour extraire les mots vides
def maker_barg_word(text):
    
    # Récupération des stopwords de la langue française depuis le module nltk
    fr_stopwords = stopwords.words('french')
    
    # Passage en minuscules pour uniformiser le texte
    cleaned_text = text.lower()
    
    # Séparation des mots du texte par espace
    words = cleaned_text.split()
    
    # Initialisation d'une liste pour stocker les mots vides
    stopwords = []
    
    # Boucle sur chaque mot du texte
    for word in words:
        
        # Vérification si le mot est un stopword
        if word in fr_stopwords:
            
            # Ajout du stopword à la liste
            stopwords.append(word)
            
    # Retourne le texte en minuscules et la liste de mots vides
    return cleaned_text, stopwords

# Chemin vers le fichier contenant le corpus à nettoyer
input_file_path = "corpus.txt"

# Chemin vers le fichier où écrire les mots vides
stopwords_file_path = "motvide.txt"

# Ouverture du fichier contenant le corpus à nettoyer en mode lecture
with open(input_file_path, 'r') as input_file:
    
    # Lecture du contenu du fichier
    text = input_file.read()
    
    # Appel de la fonction de nettoyage pour extraire les mots vides et nettoyer le texte
    cleaned_text, stopwords = mager_bag_word(text)
    
    # Ouverture du fichier où écrire les mots vides en mode écriture
    with open(stopwords_file_path, 'w') as stopwords_file:
        
        # Écriture de chaque mot vide dans le fichier
        for stopword in stopwords:
            stopwords_file.write(stopword + '\n')

