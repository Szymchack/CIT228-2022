print("--------------------10-3--------------------")
filename = 'Chapter 10/guest.txt'
name = input("What's your name (enter q to quit)? ")

with open("Chapter 10/guest.txt", 'a') as nameFile:
    while name!='q':
        name+="\n"
        nameFile.write(name)
        name = input("What's your name (enter q to quit)?")


print("--------------------10-4--------------------")

filename = 'Chapter 10/guest.txt'

print("Enter 'quit' when you are finished.")
while True:
    name = input("\nWhat's your name? ")
    if name == 'quit':
        break
    else:
        with open(filename, 'a') as f:
            f.write(f"{name}\n")
        print(f"Hi {name}, you've been added to the guest book.")