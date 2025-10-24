from swap_meet.item import Item

class Clothing(Item):
    def __init__(self, age=0, id=None, condition=0, fabric="Unknown"):
        super().__init__(age, id, condition)
        self.fabric = fabric
    
    def get_category(self):
        return "Clothing"
    
    def __str__(self):
        first_part = super().__str__()
        second_part = f"It is made from {self.fabric} fabric."
        return first_part + " " + second_part