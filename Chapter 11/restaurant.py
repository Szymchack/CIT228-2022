class Restaurant():

    def __init__(self, name, cuisine_type):
        self.name = name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_Restaurant(self):
        msg = self.name + " serves the freshest " + self.cuisine_type + " around!"
        print("\n" + msg)

    def open_Restaurant(self):
        msg = self.name + " is open, come as you are and bring your friends!"
        print("\n" + msg)

    def set_number_served(self,number_served):
        self.number_served = number_served

    def increment_number_served(self, additional_served):
        self.number_served +=additional_served



