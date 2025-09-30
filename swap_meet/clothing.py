from item import Item

class Clothing(Item):
    def __init__(self, id=None, fabric="Unknown"):
        super().__init__(id)
        self.fabric = fabric
    
    def get_category(self):
        return "Clothing"