class Materialen:
    def __init__(self, materiaalID, beschrijving):
               
        self.__materiaalID = materiaalID
        self.__beschrijving = beschrijving
       
    
    @property
    def materiaalID(self):
        return self.__materiaalID
    
    @property
    def beschrijving(self):
        return self.__beschrijving
    
    @materiaalID.setter
    def materiaalID(self, value):
        if not isinstance (value, int):
            return False
        self.__materiaalID = value

    @beschrijving.setter
    def beschrijving(self, value):
        if value == "":
            return False
        self.__beschrijving = value

        
    
    
    