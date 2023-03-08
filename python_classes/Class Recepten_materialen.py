class Recepten_materialen:
    def __init__(self, ingrediëtID, materiaalID):
               
        self.__ingrediëtID = ingrediëtID
        self.__materiaalID = materiaalID
       
    
    @property
    def ingrediëtID(self):
        return self.__ingrediëtID
    
    @property
    def materiaalID(self):
        return self.__materiaalID
    
    
    