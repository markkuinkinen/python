import math
import random

# print("Hello, Markku Inkinen")

# user = input("Type in your name: ")
# print('hello, ' + user + "!")

#1 works out area of circle with radius
radius = float(input("Type in radius of a circle to work out the area: "))
print("The area of the circle is " + str(3.14 * (radius * radius)))
print("The more precise area of the circle is " + str(math.pi * (radius**2)))

#2 works out perimeter of rectangle
length = float(input("Type in the length of the rectangle: "))
width = float(input("Type in the width of the rectangle: "))
perimeter = (length + width) * 2
print("The perimeter of the rectangle is: " + str(perimeter))

#3 sum/product/average of 3 numbers
firstNumber = float(input("Type in the first of 3 numbers: "))
secondNumber = float(input("Type in the second of 3 numbers: "))
thirdNumber = float(input("Type in the third of 3 numbers: "))

print("The sum of the numbers is: " + str(firstNumber + secondNumber + thirdNumber))
print("The product of the numbers is: " + str(firstNumber * secondNumber * thirdNumber))
print("The average of the numbers is: " + str((firstNumber + secondNumber + thirdNumber) / 3))

#4 converts talents/pounds/lots to kg and grams
talents = float(input("Enter talents: "))
pounds = float(input("Enter pounds: "))
lots = float(input("Enter lots: "))

totalGrams = (talents * 20 * 32 * 13.3) + (pounds * 32 * 13.3) + (lots * 13.3)
kg = int(totalGrams / 1000)
grams = (float(totalGrams) - (kg * 1000))
print("The weight in modern units:")
print(str(kg) + " kilograms and " + str(grams) + " grams.")

#5 creates 2 random codes (3 digit between 0-9, 4 digit between 1-6)
number1 = random.randint(0, 9)
number2 = random.randint(0, 9)
number3 = random.randint(0, 9)
print("The first random 3 digit code with numbers between 0-9: ")
print(str(str(number1)+ "-" + str(number2) + "-" + str(number3)))
print("The second random 4 digit code with numbers between 1-6: ")
print(str(random.randint(1, 6)) + "-" + str(random.randint(1, 6)) + "-" + str(random.randint(1, 6)) + "-" + str(random.randint(1, 6)))


