
import random

#1 Rolls a dice x amount of times and prints the sum
rollNumber = input("Enter amount of times to roll dice: ")
rolledNumbers = []
for x in range(int(rollNumber)):
    rolled = random.randint(1, 6)
    rolledNumbers.append(rolled)
print(sum(rolledNumbers))
print(rolledNumbers)


# rolledNumbers.sort(reverse=True)
# print(rolledNumbers[int(rollNumber) - 5:int(rollNumber)])
# print(rolledNumbers[-5:]) #goes from left to right side [5:9] 5-9


# bonus - factorial of input 
number = int(input("Enter a number: "))
factorial = 1
if number != 0:
    for i in range(1, number+1):
        factorial *= i
    print(factorial)
if number < 0:
    print("Error")


#2 User enters numbers, numbers are printed in descending order of 5 largest
enteredNumbers = []
while True:
    numberToAdd = input("Enter a number: ")
    if numberToAdd == "":
        enteredNumbers.sort(reverse=True)
        print(enteredNumbers[:5])
        break
    enteredNumbers.append(int(numberToAdd))


#3 Enter INT, checks if it's a prime number
numbers = []
numberToCheck = int(input("Enter an integer to see if it's a prime number: "))
for x in range(numberToCheck + 1):
    if x != 0 and numberToCheck % x == 0:
        numbers.append(x)
if (len(numbers)) > 2:
    print(str(numberToCheck) + " is not a prime number.")
else:
    print(str(numberToCheck) + " is a prime number.")


#3 - Second method without list
numberToCheck = int(input("Enter int to see if it's a prime number: "))
isPrime = True
for x in range(2, numberToCheck - 1):
    if numberToCheck % x == 0:
        isPrime = False
if isPrime:
    print(str(numberToCheck) + " is a prime number")
else:
    print(str(numberToCheck) + " is not a prime number")
    


#4 Enter 5 cities, prints them on their own line in order of input
cities = []
for x in range(5):
    cityName = str(input(str(x + 1) + "/5. Enter a city: "))
    cities.append(str(cityName))
for x in range(len(cities)):
    print(str(x + 1) + ". " + cities[x])

#print(*cities, sep = "\n")     #alternate way to print all cities in list, separated with line break