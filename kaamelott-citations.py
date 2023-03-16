# Importation de la librairie random
import random

# Définition de la classe PhraseAleatoire
class PhraseAleatoire:
    # Définition de la méthode d'initialisation
    def __init__(self, citations):
        self.citations = kaamelottCitations

    # Définition de la méthode get_phrase_aleatoire
    def get_phrase_aleatoire(self):
        return random.choice(self.citations)

# Utilisation
kaamelottCitations = ["Sire, avec tout le respect, est-ce que la reine a les fesses blanches ?", 
             "Putain, en plein dans sa mouille !", 
             "C’est pas faux.",
             "Après demain, à partir d'aujourd'hui ?",
             "Et toc ! Remonte ton slibard, Lothard !",
             "Ça prouve que j'ai de l'ubiquité... De l'humilité ? C'est pas quand il y a des infiltrations ?",
             "Les 3 actes, c'est les bonnes femmes qui sont mi-taupes mi-déesses, et qui ont forcé les mecs de Bethléem à construire les pyramides.",
             "Je vous ai vu une fois dans une carriole, tirée par un cheval. Enfin, la carriole tirée par un cheval.",
             "Au printemps, j’aime bien pisser du haut des remparts au lever du soleil… Y’a une belle vue !",
             "Mais cherchez pas à faire des phrases pourries... On en a gros, c'est tout !"]
             
# Instanciation de l'objet phrase
phrase = PhraseAleatoire(kaamelottCitations)
print(phrase.get_phrase_aleatoire())