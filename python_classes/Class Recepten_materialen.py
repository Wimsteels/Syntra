class Recepten_materialen:
    def __init__(self, ingrediëntID, materiaalID):
               
        self.__ingrediëntID = ingrediëntID
        self.__materiaalID = materiaalID
       
    
    @property
    def ingrediëntID(self):
        return self.__ingrediëntID
    
    @property
    def materiaalID(self):
        return self.__materiaalID
    
    @ingrediëntID.setter
    def ingrediëntID(self, value):
        if not isinstance(value, int):
            return False
        self.__ingrediëntID = value

    @materiaalID.setter
    def materiaalID(self, value):
        if not isinstance(value, int):
            return False
        self.__materiaalID = value
    
    
    