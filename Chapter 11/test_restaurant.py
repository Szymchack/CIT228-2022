import unittest

from restaurant import restaurant

black_opal = Restaurant('the black opal', 'seafood')
black_opal.describe_restaurant()

maestro = restaurant("maestro's", 'italian')
maestro.describe_restaurant()

mimi = restaurant("mimi's", 'home cooking')
mimi.describe_restaurant()

print("Below printed by setting attribute")
restaurant.number_served = 56
print("Below printed by method")
restaurant.set_number_served = 14
print("Below is printed with increment method")
restaurant.increment_number_served = 200 

restaurant = Restaurant('the black opal', 'seafood')