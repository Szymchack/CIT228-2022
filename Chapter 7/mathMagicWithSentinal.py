import random
prompt = "Would you like to play Math Magic?"
prompt +=" Enter 'q' to end the program"
keepGoing = ""
while keepGoing != 'q':
    randNumber1 = random.randrange(1, 1000)
    randNumber2 = random.randrange(1, 1000)
    correctAnswer = int(randNumber1 + randNumber2)
    yourAnswer = int(input(f"What is the integer value of {randNumber1} + {randNumber2}?"))
    if correctAnswer==yourAnswer:
        print("Awesomeness, you did it!")
    else:
        print("Well, better luck next time!")
    keepGoing = input(prompt)
    
    print("Thanks for playing Math Magic")