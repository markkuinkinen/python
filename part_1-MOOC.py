
# #Getting started
# Write your solution here
print(":-)")


# Fix the code
print("Aapo")
print("Eero")
print("Juhani")
print("Lauri")
print("Simeoni")
print("Timo")
print("Tuomas")


# Write your solution here
print("Row, row, row your boat,\nGently down the stream.\nMerrily, merrily, merrily, merrily,\nLife is but a dream.")


# Write your solution here
print("Minutes in a year")
print(365*24*60) # 365 days, 24 hours, 60 minutes


# Write your solution here
print('print("Hello there!")')


#Information from the user
# Write your solution here
name = input("What is your name? ")
print(name)
print(name)


# Write your solution here
name = input("What is your name? ")
print("!" + name + "!" + name + "!")


# Write your solution here
given_name = input("Given name: ")
family_name = input("Family name: ")
street_address = input("Street address: ")
city_postalCode = input("City and postal code: ")
print(given_name + " " + family_name)
print(street_address)
print(city_postalCode)


# Fix the code
part1 = input("The 1st part: ")
part2 = input("The 2nd part: ")
part3 = input("The 3rd part: ")
print(part1 + "-" + part2 + "-" + part3 + "!")


# Write your solution here
name = input("Please type in a name: ")
year = input("Please type in a year: ")

print(name + " is a valiant knight, born in the year " + year + ". One morning " + name + 
" woke up to an awful racket: a dragon was approaching the village. Only " + name + " could save the village's residents.")


# More about variables
name = "Tim Tester"
age = 20
skill1 = "python"
level1 = "beginner"
skill2 = "java"
level2 = "veteran"
skill3 = "programming"
level3 = "semiprofessional"
lower = 2000
upper = 3000

print(f"my name is {name}, I am {age} years old\n")
print("my skills are")
print(f" - {skill1} ({level1})")
print(f" - {skill2} ({level2})")
print(f" - {skill3} ({level3})\n")
print(f"I am looking for a job with a salary of {lower}-{upper} euros per month")


# Write your solution here
x = 27
y = 15

print(f"{x} + {y} = {x+y}")
print(f"{x} - {y} = {x-y}")
print(f"{x} * {y} = {x*y}")
print(f"{x} / {y} = {x/y}")


# Fix the code
print(5, end="")
print(" + ", end="")
print(8, end="")
print(" - ", end="")
print(4, end="")
print(" = ", end="")
print(5 + 8 - 4, end="")


#Arithmetic operations
# Write your solution here
number = int(input("Please type in a number: "))
print(f"{number} times 5 is {number * 5}")


# Write your solution here
name = input("What is your name? ")
birthYear = int(input("Which year were you born? "))
print(f"Hi {name}, you will be {2021 - birthYear} years old at the end of the year 2021")


# Write your solution here
days = int(input("How many days? "))
print(f"Seconds in that many days: {days * 24 * 60 * 60}")


# Fix the code
number1 = int(input("Please type in the first number: "))
number2 = int(input("Please type in the second number: "))
number3 = int(input("Please type in the third number: "))

product = number1 * number2 * number3

print("The product is", product)


# Write your solution here
number1 = int(input("Number 1: "))
number2 = int(input("Number 2: "))
print(f"The sum of the numbers: {number1 + number2}")
print(f"The product of the numbers: {number1 * number2}")


# Write your solution here
sum = 0

sum += int(input("Number 1: "))
sum += int(input("Number 2: "))
sum += int(input("Number 3: "))
sum += int(input("Number 4: "))

print(f"The sum of the numbers is {sum} and the mean is {sum / 4}")


# Write your solution here
visits = int(input("How many times a week do you eat at the student cafeteria? "))
lunchPrice = float(input("The price of a typical student lunch? "))
groceries = float(input("How much money do you spend on groceries in a week? "))

print("\nAverage food expenditure:")
print(f"Daily: {(visits * lunchPrice + groceries) / 7} euros")
print(f"Weekly: {visits * lunchPrice + groceries} euros")


# Write your solution here
import math
students = int(input("How many students on the course? "))
groupSize = int(input("Desired group size? "))

print(f"Number of groups formed: {math.ceil(students / groupSize)}")


# Conditional statemements
# Write your solution here
number = input("Please type in a number: ")
if number == str(1984):
    print("Orwell")


# Write your solution here
number = input("Please type in a number: ")
if int(number) < 0:
    print(f"The absolute value of this number is {int(number) * -1}")
else:
    print("The absolute value of this number is", number)

# Write your solution here
name = input("Please tell me your name: ")
if str(name) == "Jerry":
    print("Next please!")
else:
    portion_numer = int(input("How many portions of soup? "))
    print("The total cost is", portion_numer * 5.90)
    print("Next please!")


# Write your solution here
number = int(input("Please type in a number: "))
if number < 1000:
    print("This number is smaller than 1000")
if number < 100:
    print("This number is smaller than 100")
if number < 10:
    print("This number is smaller than 10")
print("Thank you!")


# Write your solution here
num1 = int(input("Number 1: "))
num2 = int(input("Number 2: "))
operation = input("Operation: ")
if operation == "add":
    print(f"{num1} + {num2} = {num1 + num2}")
if operation == "multiply":
    print(f"{num1} * {num2} = {num1 * num2}")
if operation == "subtract":
    print(f"{num1} - {num2} = {num1 - num2}")


# # Write your solution here
temp_f = int(input("Please type in a temperature (F): "))
converted_temp = (temp_f - 32) * (5/9)
print(f"{temp_f} degrees Fahrenheit equals {converted_temp} degrees Celsius")
if converted_temp < 0:
    print("Brr! It's cold in here!")


# Write your solution here
wage = float(input("Hourly wage: "))
hours = float(input("Hours worked: "))
day = input("Day of the week: ")
if str(day) == "Sunday":
    print(f"Daily wages: {(wage * hours) * 2} euros")
else:
    print(f"Daily wages: {wage * hours} euros")


# Fix the program
points = int(input("How many points are on your card? "))
if points < 100:
    points *= 1.1
    print("Your bonus is 10 %")

elif points >= 100:
    points *= 1.15
    print("Your bonus is 15 %")

print("You now have", points, "points")


# Write your solution here
print("What is the weather forecast for tomorrow?")
temp = int(input("Temperature: "))
raining = str(input("Will it rain (yes/no): "))

print("Wear jeans and a T-shirt")

if temp <= 20: 
    print("I recommend a jumper as well")
if temp <= 10:
    print("Take a jacket with you")
if temp <= 5:
    print("Make it a warm coat, actually\nI think gloves are in order")
if raining == "yes":
    print("Don't forget your umbrella!")


# Write your solution here
# Let's take the square root of math-module in use
from math import sqrt

a = float(input("Value of a: "))
b = float(input("Value of b: "))
c = float(input("Value of c: "))

root1 = (-b + sqrt((b**2) - (4 * a * c)))/(2 * a)
root2 = (-b - sqrt((b**2) - (4 * a * c)))/(2 * a)
print(f"The roots are {root1} and {root2}")
