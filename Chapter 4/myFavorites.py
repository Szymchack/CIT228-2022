foods=["Pot Roast", "Chicken Oriental Salad", "Chimichanga", "Asain Chicken and Green Beans", "Bacon", "Barbeque"]
print(f"Favorite food:{foods[0], foods[1], foods[2], foods[3], foods[4], foods[5]}")
print("----------------------------------------------")
numbers=["8", "88", "10", "5", "23", "3"]
print(f"Favorite number:{numbers[0], numbers[1], numbers[2], numbers[3], numbers[4], numbers[5]}")
print("-----------------------------------------------")
movies=["Harry Potter", "Race to Witch Mountain", "Transformers"]
print(f"Favorite movie:{movies[0], movies[1], movies[2]}")
print("------------------------------------------------")
print(f"My combo list: {foods[0]}, {foods[-1]}, {numbers[0]}, {numbers[1]}, {movies[0]}, {movies[1]}")
print("------------------------------------------------")
print(f"Last food item: {foods[-1]}")
print("------------------------------------------------")
print(f"2nd, 4th, and 6th number: {numbers[1]}, {numbers[3]}, {numbers[-1]}")
print("------------------------------------------------")
print(f"All Movies: {movies[0]}, {movies[1]}, {movies[2]}")
print("------------------------------------------------")
print(f"First food, First number, First movie: {foods[0]}, {numbers[0]}, {movies[0]}")
print("-------------------------------------------------")
movies.append('Calamity Jane')
print(movies)
print("-------------------------------------------------")
numbers.insert(3, '25')
print(numbers)
print("-------------------------------------------------")
foods.insert(5, 'Cream Cheese')
print(foods)
print("-------------------------------------------------")
del foods[5]
print(foods)
print("-------------------------------------------------")
popped_numbers=numbers.pop()
print(numbers)
print(popped_numbers)
print("-------------------------------------------------")
popped_2=numbers.pop(2)
print(numbers)
print(popped_2)
print("-------------------------------------------------")
print("Here is the Original List:" )
print((movies))
print("/nHere is the Sorted List:")
print(sorted(movies))
print("-------------------------------------------------")
print("Here is the Sorted List of foods:")
print(sorted(foods))
print("-------------------------------------------------")
print("Here is the Original List:" )
print((numbers))
print("\nHere is the Sorted List:")
print(sorted(numbers))
print("\nHere is the Original List Again:")
print(numbers)
print("-------------------------------------------------")
print(movies)
movies.reverse()
print(movies)

print("---------------Chapter 4 Hands On 1-------------")

print("Foods List")
print("---------------------------------------")

for item in foods:
    print(item)
    
print("Numbers List")
print("---------------------------------------")

for item in numbers:
    print(item)
    
print("Movies List")
print("---------------------------------------")

for item in movies:
    print(item)
    
print("Foods")
print("---------------------------------------")

combolist=["Pot Roast", "Chicken Oriental Salad", "8", "88", "Harry Potter", "Race To Witch Mountain"]
for combo in combolist:
    print(combo)