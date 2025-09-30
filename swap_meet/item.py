import uuid
class Item:
    def __init__(self, id=None):
        
        if id is None:
            unique_id = uuid.uuid4()
            self.id = unique_id.int
        else:
            self.id = id    
        # self.id = unique_id.UUID.int

        # self.id = unique_id.UUID.int
        # unique_id = UUID.int
        

    def get_category(self):
        return "Item"       