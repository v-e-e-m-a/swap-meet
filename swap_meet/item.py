import uuid

class Item:
    def __init__(self, id=None, condition=0):
        # If no id is passed through, program will make one using uuid and assign it to id
        if id is None:
            self.id_as_uuid = uuid.uuid4()
            self.id = self.id_as_uuid.int
        else:
            self.id = id
        self.condition = condition
    
    def get_category(self):
        # Returns a string of the class name
        return "Item" #implementation obtained through StackOverflow
    
    def __str__(self): #Operator overloading the str() function when it passes through an item in the argument
        return f'An object of type {self.get_category()} with id {self.id}.'
    
    def condition_description(self):
        # Chose to use a dictionary over a list for better time complexity (O(1) vs O(n))
        DESCRIPTIONS = {
            0: "Is it worth getting at this point?",
            1: "I guess it's better than nothing.",
            2: "Maybe the dog will like it.",
            3: "This can be my back up.",
            4: "What a find!",
            5: "Unicorn"
        }
        return DESCRIPTIONS[self.condition]