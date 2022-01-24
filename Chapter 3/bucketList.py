places=["Grand Canyon", "Chichen Itza", "Machu Picchu", "Jerusalem", "Teotihuacan", "Ireland"]
print(f"My Bucket List: {places}")

places.append('Scotland')
places.insert(0, 'Oak Island')
print(f"My list after additions: {places}")

del places[0]
popped_places=places.pop()
print(f"My list after deletions: {places}")

print("\nList with temporary sort")
print(sorted(places))

places.reverse()
print(f"List in reverse: {places}")

len(places)
print(f"This is my number of places:{len(places)}")