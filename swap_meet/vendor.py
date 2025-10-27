from .item import Item
class Vendor:
    def __init__(self, inventory=None):
        self.inventory = [] if inventory is None else inventory[:]
        

    def add(self,item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        if item not in self.inventory:
            return False
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
    
    def get_by_category(self, category):
        if self.inventory == []:
            return []
        category_list = []
        for item in self.inventory:
            if item.get_category() == category:
                category_list.append(item)
        return category_list
    
    def get_best_by_category(self, category):
        category_list = self.get_by_category(category)
        if category_list == []:
            return None
        best_score = 0
        for item in category_list:
            if item.condition > best_score:
                best_score = item.condition
                best_item = item
        return best_item
    
    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        item_to_swap = self.get_best_by_category(their_priority)
        their_item = other_vendor.get_best_by_category(my_priority)

        if item_to_swap and their_item:
            self.swap_items(other_vendor, item_to_swap, their_item)
            return True
        return False
    def swap_by_newest(self, other_vendor):
        if not self.inventory or not other_vendor.inventory:
            return False
        newest_item = self.inventory[0]
        for item in self.inventory:
            if item.age < newest_item.age:
                newest_item = item
        newest_other_vendor = other_vendor.inventory[0]        
        for item in other_vendor.inventory:
            if item.age < newest_other_vendor.age:
                newest_other_vendor = item
        self.swap_items(other_vendor, newest_item, newest_other_vendor)
        return True                       
    

    
