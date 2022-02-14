import random
counter=0
numberCorrect=0
numberIncorrect=0
while counter < 10:
    randNumber1 = random.randrange(1, 1000)
    randNumber2 = random.randrange(1, 1000)
    correctAnswer = int(randNumber1 + randNumber2)
    yourAnswer = int(input(f"What is the integer value of {randNumber1} + {randNumber2}?"))
    if correctAnswer==yourAnswer:
        print("Awesomeness, that is correct ",correctAnswer) 
        numberCorrect +=1
    else:
        print("Im sorry that is incorrect.")
        numberIncorrect +=1
        
    if numberIncorrect <5:
        print("Im sorry that is more than 5 incorrect.  You should probably get a tuitor.")
        
        