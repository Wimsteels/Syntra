class Recepten_ingrediënten:
    def __init__(self, receptID, ingrediëntID, alternatief_ingrediëntID, hoeveelheid, eenheid):
               
        self.__receptID = receptID
        self.__ingrediëntID = ingrediëntID
        self.__alternatief_ingrediëntID = alternatief_ingrediëntID
        self.__hoeveelheid = hoeveelheid
        self.__eenheid = eenheid
        
    @property
    def receptID(self):
        return self.__receptID
    
    @property
    def ingrediëntID(self):
        return self.__ingrediëntID
    
    @property
    def alternatief_ingrediëntID(self):
        return self.__alternatief_ingrediëntID
    
    @property
    def hoeveelheid(self):
        return self.__hoeveelheid

    @property
    def eenheid(self):
        return self.__eenheid


