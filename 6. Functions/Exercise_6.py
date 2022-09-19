import random
import math
from turtle import circle

# 1 Function that returns random dice roll between 1-6, write main that stops when 6 is hit
def rollDice():
    rolledNumber = random.randint(1,6)
    return rolledNumber

while True:
    number = rollDice()
    print(number)
    if number == 6:
        print("6 was finally hit. Now stopping...")
        break


# 2 Above function modified to take number of sides as a paramete, stops when it gets the max possible roll
def rollDice(numberOfSides):
    rolledNumber = random.randint(1, numberOfSides)
    return rolledNumber

userNumber = input("Enter amount of sides the dice has: ")
while True:
    number = rollDice(int(userNumber))
    print(number)
    if number == int(userNumber):
        print("Highest roll was finally hit. Now stopping...")
        break


# 3 Function that takes gallons and converts it to litres, continues until user inputs negative number
def convertGallons(amount):     # 1 Gallon = 3.78541 Litres
    result = float(amount * 3.78541)
    return result

while True:
    userInput = input("Enter amount of gallons to convert to litres: ")
    if float(userInput) < 0:
        break
    print(convertGallons(float(userInput)))


# 4 Function that returns the sum of a list of ints 
def sumOfList(list):
    sumOfList = 0
    for x in range(len(list)):
        sumOfList += list[x]
    return sumOfList

list = [5, 10, 15]
print(sumOfList(list))


# 5 Function that returns the sum of a list of ints WITHOUT even numbers
def removeEvenFromList(list):
    newList = []
    for x in range(len(list)):
        if list[x] % 2 == 0:
            newList.append(list[x])
    return newList

numberList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
print(removeEvenFromList(numberList))
print(numberList)


#6 Takes 2 parameters (diameter of pizza in cm, price of pizza in euros) and calculated the price of pizza per square meter, compares two pizzas and tells cheapest
def pizzaSizeCost(size, cost):
    pizzaArea = math.pi * (size/2)**2 #in cm^2
    costInCents = float(cost)/100   #in cents
    costForSize = (float(costInCents) / pizzaArea) * 100   #convert to metres and euros
    return costForSize * 10000

def pizzaSizeCost(size, cost):
    result = ((math.pi * ((size/2)**2)) / 10000) / cost
    result2 = ((10000 * cost) / (math.pi * ((size/2)**2)))
    return result2

firstPizzaSize = input("Enter the diameter of the first pizza in cm: ")
firstPizzaCost = input("Enter the cost of the first pizza in euros: ")
secondPizzaSize = input("Enter the diameter of the second pizza in cm: ")
secondPizzaCost = input("Enter the cost of the second pizza in euros: ")

firstPizzaValue = pizzaSizeCost(float(firstPizzaSize), float(firstPizzaCost))
secondPizzaValue = pizzaSizeCost(float(secondPizzaSize), float(secondPizzaCost))

if (firstPizzaValue > secondPizzaValue):
    print("The first pizza is cheaper at " + str(firstPizzaValue) + " euros per square meter compared to " + str(secondPizzaValue) + " euros per square meter")
elif (firstPizzaValue < secondPizzaValue):
    print("The second pizza is cheaper at " + str(secondPizzaValue) + " euros per square meter compared to " + str(firstPizzaValue) + " euros per square meter")
else:
    print("They are the same cost at " + str(firstPizzaValue) + " euros per square meter")