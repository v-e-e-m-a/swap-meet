import uuid
class Item:
    def __init__(self, age=0, id=None, condition=0):
        self.id = uuid.uuid4().int if id is None else id   
        self.age = age   
        self.condition = condition      

    def get_category(self):
        return "Item"   

    def __str__(self):
        return f"An object of type {self.get_category()} with id {self.id}."    

    def condition_description(self):
        description_tuples = [
            (5.0, "Like new"),     
            (4.0, "Very good"),     
            (3.0, "Good"),          
            (2.0, "Fair"),         
            (1.0, "Gently used"),   
            (0.0, "Heavily used")   
        ]
        
        for condition, description in description_tuples:
            if self.condition >= condition:
                return description