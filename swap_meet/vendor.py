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
    
    def swap_items(self, other_vendor, my_item, their_item):
        #Checks if items are located in the correct starting vendor
        if my_item in self.inventory and their_item in other_vendor.inventory:
            self.remove(my_item)
            other_vendor.remove(their_item)
            self.add(their_item)
            other_vendor.add(my_item)
            return True
        else:
            return False
    
    def swap_first_item(self, other_vendor):
        if self.inventory == [] or other_vendor.inventory == []:
            return False
        else:
            my_item = self.inventory[0]
            their_item = other_vendor.inventory[0]

            self.remove(my_item)
            other_vendor.remove(their_item)

            self.add(their_item)
            other_vendor.add(my_item)

            return True