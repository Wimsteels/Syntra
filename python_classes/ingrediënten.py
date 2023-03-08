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
    
    @ingrediëntID.setter
    def ingrediëntID(self, value):
        if not isinstance (value, int):
            return False
        self.__ingrediënt_categorie = value

    @ingrediëntnaam.setter
    def ingrediëntnaam(self, value):
        if value == "":
            return False
        self.__ingrediëntnaam = value

    @kleur.setter
    def kleur(self, value):
        if value == "":
            return False
        self.__kleur = value
    
    @ingrediënt_categorie.setter
    def ingrediënt_categorie(self, value):
        if value == "":
            return False
        self.ingrediënt_categorie = value
    
    @hoeveelheid_in_stock.setter
    def hoeveelheid_in_stock(self, value):
        if not isinstance (value, float, int):
            return False
        self.__hoeveelheid_in_stock = value

    @eenheid_in_stock.setter
    def eenheid_in_stock(self, value):
        if value == "":
            return False
        self.__eenheid_in_stock = value
