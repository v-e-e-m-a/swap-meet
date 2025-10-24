from swap_meet.item import Item

class Electronics(Item):
    def __init__(self, age=0, id=None, condition=0, type="Unknown"):
        super().__init__(age, id, condition)
        self.type = type

    def get_category(self):
        return "Electronics"
    
    def __str__(self):
        first_part = super().__str__()
        second_part = f"This is a {self.type} device."
        return first_part + " " + second_part
