import json

class Person:
    # Création d'une méthode __init__ avec les arguments "age", "firstname" et "gender"
    def __init__(self, age, firstname, gender):
        # Création d'un attribut "dictionnaire" avec les valeurs "age", "firstname" et "gender"
        self.dictionnaire = {
            'age': age,
            'firstname': firstname,
            'gender': gender
        }
        
    # Création d'une méthode "set_dictionnaire" avec l'argument "dictionnaire"
    def set_dictionnaire(self, dictionnaire):
        # L'attribut "dictionnaire" de la classe Person prend la valeur de l'argument "dictionnaire"
        self.dictionnaire = dictionnaire
        
    # Création d'une méthode "to_json"
    def to_json(self):
        # Retourne la valeur de l'attribut "dictionnaire" de la classe Person
        return json.dumps(self.dictionnaire)
    
# Création d'une instance de la classe Person avec les arguments "35", "Jean" et "masculin"
person1 = Person(35, 'Germain', 'masculin')
print(person1.to_json())

# Appelle la méthode "set_dictionnaire" de l'instance "person1" avec l'argument "{'age': 25, 'firstname': 'Marie', 'gender': 'feminin'}"
person1.set_dictionnaire({'age': 25, 'firstname': 'Marie', 'gender': 'feminin'})
print(person1.to_json())
