class Vendor:
    def __init__(self, inventory = None):
        if inventory is None:
            self.inventory = []
        else:
            self.inventory = inventory[:]
        

    def add(self,item):
        self.inventory.append(item)
        return item
    
    def remove(self, item):
        if item not in self.inventory:
            return False
        else:
            self.inventory.remove(item)
            return item    

    def get_by_id(self, item_id):
        for item in self.inventory:
            if item.id == item_id:
                return item
        else:
            return None