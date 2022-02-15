from restaurant import Restaurant
from icecream import IceCreamStand

black_opal = Restaurant('the black opal', 'seafood')
black_opal.describe_restaurant()

maestro = Restaurant("maestro's", 'italian')
maestro.describe_restaurant()

mimi = Restaurant("mimi's", 'home cooking')
mimi.describe_restaurant()

cats_cream = IceCreamStand('Cats Cream Ice Cream')
cats_cream.flavors = ['blue moon', 'vanilla', 'chocolate', 'cheesecake'] 
cats_cream.describe_restaurant()
cats_cream.show_flavors()