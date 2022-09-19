from platform import python_branch
import random
import math

#1 Prints all numbers divisible by 3 in a range of 1-1000
startingNumber = 1
while startingNumber <= 1000:
    if startingNumber % 3 == 0:
        print(startingNumber)
    startingNumber += 1


# #2 Converts inches to cm
while True:
    inches = float(input("Enter amount of inches you want to convert to cm: "))
    if (inches < 0):
        break
    elif inches > 0:
        print(str(inches * 2.54))

# #3 - method 1 User enters numbers which are added to a list, empty input returns largest and smallest number added
numlist = []
while True:
    inputData = input("Add input: ")
    if inputData == "":
        print(max(numlist))
        print(min(numlist))
        break
    numlist.append(float(inputData))


# #3 - method 2 User enters numbers which are added to a list, empty input returns largest and smallest number added
smallestNum = 32**2
largestNum = -32**2
while True:
    userInput = input("Enter a value: ")
    if userInput == "":
        print(smallestNum)
        print(largestNum)
        break   
    if smallestNum == 0 and largestNum == 0:
        if float(userInput) != 0:
            if float(userInput) < 0:
                smallestNum = float(userInput)
            else:
                largestNum = float(userInput)
    userNumber = float(userInput)
    if userNumber < smallestNum:
        smallestNum = userNumber
    if userNumber > largestNum:
        largestNum = userNumber


# 4 Creates random number, user has to guess it
intToGuess = random.randint(1, 10)
while True:
    userGuess = int(input("Guess which number I'm thinking of between 1-10: "))
    if userGuess == intToGuess:
        print("Correct!")
        break
    if userGuess < intToGuess:
        print("Too low.")
    if userGuess > intToGuess:
        print("Too high.")



#5 Asks for username and password until correct, tells how many attempts remaining
username = "python"
password = "rules"
attempts = 4
while attempts >= 0:
    givenUserName = str(input("Username: "))
    givenPassword = str(input("Password: "))
    if givenUserName != username or givenPassword != password:
        print("Wrong credentials. " + str(attempts) + " attempts remaining.")
        attempts -= 1
        if attempts < 0:
            print("Access denied")
            break 
    else:
        print("Welcome!")
        break


#6 Assumes approx. of pi (circle in square)
counter = 0
circleCounter = 0
while True:
    userInput = int(input("Type amount of points to calculate approximation of pi: "))
    while (counter <= userInput):
        xPosition = random.uniform(0, 1)
        yPosition = random.uniform(0, 1)
        if xPosition**2 + yPosition**2 < 1:
            circleCounter += 1
        counter += 1
    piApprox = float((4 * circleCounter) / userInput)
    print(piApprox)
    break