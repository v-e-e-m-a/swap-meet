import uuid

class Item:
    def __init__(self, id=None):
        # If no id is passed through, program will make one using uuid and assign it to id
        if id is None:
            self.id_as_uuid = uuid.uuid4()
            self.id = self.id_as_uuid.int
        else:
            self.id = id
    
    def get_category(self):
        # Returns a string of the class name
        return str(self.__class__.__name__) #implementation obtained through StackOverflow