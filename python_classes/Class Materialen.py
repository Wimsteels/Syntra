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
    
    
    