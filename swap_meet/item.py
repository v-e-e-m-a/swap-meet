import uuid
class Item:
    def __init__(self, id=None, condition=0):
        
        if id is None:
            unique_id = uuid.uuid4()
            self.id = unique_id.int
        else:
            self.id = id         

        self.condition = condition      

    def get_category(self):
        return "Item"   

    def __str__(self):
        return f"An object of type Item with id {self.id}."    
    
    def condition_description(self):
        descriptions = {
            0: "Heavily used",
            1: "Gently used",
            2: "Fair",
            3: "Good",
            4: "Very good",
            5: "Like new"
        }
        return descriptions.get(self.condition)