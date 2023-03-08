class Ingrediënten:
    def __init__(self, ingrediëntID, ingrediëntnaam, kleur, ingrediënt_categorie, hoeveelheid_in_stock, eenheid_in_stock):
               
        self.__ingrediëntID = ingrediëntID
        self.__ingrediëntnaam = ingrediëntnaam
        self.__kleur = kleur
        self.__ingrediënt_categorie = ingrediënt_categorie
        self.__hoeveelheid_in_stock = hoeveelheid_in_stock
        self.__eenheid_in_stock = eenheid_in_stock
        
    
    @property
    def ingrediëntID(self):
        return self.__ingrediëntID
    
    @property
    def ingrediëntnaam(self):
        return self.__ingrediëntnaam
    
    @property
    def kleur(self):
        return self.__kleur

    @property
    def ingrediënt_categorie(self):
        return self.__ingrediënt_categorie

    @property
    def hoeveelheid_in_stock(self):
        return self.__hoeveelheid_in_stock

    @property
    def eenheid_in_stock(self):
        return self.__eenheid_in_stock