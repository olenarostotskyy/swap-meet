from swap_meet.item import Item


class Decor(Item):
     def __init__(self,category="Decor",condition=0,age=0):
        #super().__init__(inventory)
        self.category=category
        self.condition=condition
        self.age=age


     def __str__(self):
        return (f"Something to decorate your space.") 