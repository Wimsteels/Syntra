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
    
    @receptID.setter
    def receptID(self, value):
        if not isinstance(value, int):
            return False
        self.__receptID = value

    @ingrediëntID.setter
    def ingrediëntID(self, value):
        if not isinstance(value, int):
            return False
        self.__ingrediëntID = value

    @alternatief_ingrediëntID.setter
    def alternatief_ingrediëntID(self, value):
        if not isinstance(value, int):
            return False
        self.__alternatief_ingrediëntID = value

    @hoeveelheid.setter
    def hoeveelheid(self, value):
        if not isinstance(value, float, int):
            return False
        self.__hoeveelheid = value

    @eenheid.setter
    def eenheid(self, value):
        if value == '':
            return False
        self.__eenheid = value


