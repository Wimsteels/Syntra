class Recepten:
    def __init__(self, receptID, receptnaam, bereidingswijze):
        #assert isinstance(receptnaam, str) and len(receptnaam)<46, 'Receptnaam moet tekst zijn en maximaal 45 karakters.'
        #assert type(bereidingswijze) == str and len(bereidingswijze)<1001, 'Bereidingswijze moet tekst zijn.'
        
        self.__receptID = receptID
        self.__receptnaam = receptnaam
        self.__bereidingswijze = bereidingswijze
        
    @property
    def receptID(self):
        return self.__receptID
    
    @property
    def receptnaam(self):
        return self.__receptnaam
    
    @property
    def bereidingswijze(self):
        return self.__bereidingswijze
    
    @receptID.setter
    def receptID(self, value):
        if not isinstance(value, int):
            return False
        self.__receptID = value

    @receptnaam.setter
    def receptnaam(self, value):
        if value == '':
            return False
        self.__receptnaam = value

    @bereidingswijze.setter
    def bereidingswijze(self, value):
        if value == '':
            return False
        self.__bereidingswijze = value


#Recept1 = Recepten(1, 'Erwtensoep', 'Stoof de groenten aan, bevochtig met water en bouillon, laat 1u zachtjes koken, mix, smaak af.')

#Recept1.__receptnaam = 'Preisoep'
#print(Recept1.receptnaam) 