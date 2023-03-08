class Categoriën:
    def __init__(self, ingrediënt_categorie):
               
        self.__ingrediënt_categorie = ingrediënt_categorie
       
    
    @property
    def ingrediënt_categorie(self):
        return self.__ingrediënt_categorie
    
    