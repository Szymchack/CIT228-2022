from restaurant import Restaurant
class IceCreamStand(Restaurant):

    def __init__(self, name, cuisine_type = 'ice_cream'):
        super().__init__(name, cuisine_type)
        self.flavors=[]

    def show_flavors(self):
        print("\nWe have the following flavors available:")
        for flavor in self.flavors:
            print(f"- {flavor.title()}")