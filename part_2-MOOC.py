#PART 2 - Programming terminology

# Fix the program
number = int(input("Please type in a number: "))
if number > 100:
    print("The number was greater than one hundred")
    number -= 100
    print("Now its value has decreased by one hundred")
    print("Its value is now "+ str(number))
print(str(number) + " must be my lucky number!")
print("Have a nice day!")


# Write your solution here
word = input("Type in a word: ")
wordLength = len(str(word))
if wordLength > 1:
    print(f"There are {wordLength} letters in the word {word}")
print("Thank you!")


# Write your solution here
number = float(input("Please type in a number: "))
print(f"Integer part: {int(number)}")
print(f"Decimal part: {number - int(number)}")


# Write your solution here
age = input("How old are you? ")
if int(age) >= 18:
    print("You are of age!")
else:
    print("You are not of age!")


# Write your solution here
num1 = int(input("Please type in the first number: "))
num2 = int(input("Please type in the second number: "))
if num1 > num2:
    print("The greater number was:", num1)
elif num2 > num1:
    print("The greater number was:", num2)
else:
    print("The numbers are equal!")


# Write your solution here
print("Person 1:")
name1 = input("Name: ")
age1 = int(input("Age: "))
print("Person 2:")
name2 = input("Name: ")
age2 = int(input("Age: "))

if age1 > age2:
    print(f"The elder is {name1}")
elif age1 < age2:
    print(f"The elder is {name2}")
else:
    print(f"{name1} and {name2} are the same age")


# Write your solution here
word1 = input("Please type in the 1st word: ")
word2 = input("Please type in the 2nd word: ")

if word1 > word2:
    print(f"{word1} comes alphabetically last")
elif word1 < word2:
    print(f"{word2} comes alphabetically last")
else:
    print("You gave the same word twice.")


# Write your solution here
age = int(input("What is your age? "))
if age < 0:
    print("That must be a mistake")
elif age >= 0 and age < 5:
    print("I suspect you can't write quite yet...")
else:
    print(f"Ok, you're {age} years old")


# Write your solution here
name = str(input("Please type in your name: "))
if name == "Huey" or name == "Dewey" or name == "Louie":
    print("I think you might be one of Donald Duck's nephews.")
elif name == "Morty" or name == "Ferdie":
    print("I think you might be one of Mickey Mouse's nephews.")
else:
    print("You're not a nephew of any character I know of.")


# Write your solution here
points = int(input("How many ponts [0-100]: "))
if points < 0 or points > 100:
    print("Grade: impossible!")
elif points >= 0 and points <= 49:
    print("Grade: fail")
elif points >= 50 and points <= 59:
    print("Grade: 1")
elif points >= 60 and points <= 69:
    print("Grade: 2")
elif points >= 70 and points <= 79:
    print("Grade: 3")
elif points >= 80 and points <= 89:
    print("Grade: 4")
else:
    print("Grade: 5")


# Write your solution here
number = int(input("Number: "))
if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
elif number % 3 == 0:
    print("Fizz")
elif number % 5 == 0:
    print("Buzz")


# Write your solution here
year = int(input("Please type in a year: "))
if year % 100 == 0:
    if year % 400 == 0:
        print("That year is a leap year.")
    else:
        print("That year is not a leap year.")
elif year % 4 == 0:
    print("That year is a leap year.")
else:
    print("That year is not a leap year.")


# Write your solution here
letter1 = str(input("1st letter: "))
letter2 = str(input("2nd letter: "))
letter3 = str(input("3rd letter: "))

if letter1 > letter2 and letter1 > letter3:     #when 1 is the highest
    if letter2 > letter3:
        print("The letter in the middle is", letter2)
    else:
        print("The letter in the middle is", letter3)
elif letter2 > letter1 and letter2 > letter3:   #when 2 is the highest
    if letter1 > letter3:
        print("The letter in the middle is", letter1)
    else:
        print("The letter in the middle is", letter3)
elif letter3 > letter1 and letter3 > letter2:   #when 3 is the highest
    if letter1 > letter2:
        print("The letter in the middle is", letter1)
    else:
        print("The letter in the middle is", letter2)


# Write your solution here
value = int(input("Value of gift: "))

if value < 5000:
    print("No tax!")
if value >= 5000 and value < 25000:
    print(f"Amount of tax: {100 + (value - 5000) * 0.08} euros")
if value >= 25000 and value < 55000:
    print(f"Amount of tax: {1700 + (value - 25000) * 0.1} euros")
if value >= 55000 and value < 200000:
    print(f"Amount of tax: {4700 + (value - 55000) * 0.12} euros")
if value >= 200000 and value < 1000000:
    print(f"Amount of tax: {22100 + (value - 200000) * 0.15} euros")
if value >= 1000000:
    print(f"Amount of tax: {142100 + (value - 1000000) * 0.17} euros")


# Write your solution here
while True:
    print("hi")
    userinput = str(input("Shall we continue? "))
    if userinput == "no":
        print("okay then")
        break


from math import sqrt
# Write your solution here

while True:
    number = int(input("Please type in a number: "))
    if number < 0:
        print("Invalid number")
    elif number == 0:
        print("Exiting...")
        break
    else:
        print(sqrt(number))


number = 5
print("Countdown!")
while True:
    print(number)
    number = number - 1
    if number == 0:
        break
print("Now!")


# Write your solution here
password = str(input("Password: "))
set_password = password
while True:
    repeat_password = str(input("Repeat password: "))
    if repeat_password == set_password:
        print("User account created!")
        break
    else:
        print("They do not match!")


# Write your solution here
pinCount = 1
while True:
    pin = str(input("PIN: "))
    if pin == "4321" and pinCount == 1:
        print("Correct! It only took you one single attempt!")
        break
    elif pin == "4321" and pinCount > 1:
        print(f"Correct! It took you {pinCount} attempts")
        break
    else:
        print("Wrong")
        pinCount += 1


# Write your solution here
year = int(input("Year: "))
yearChecker = year + 1
while True:
    if yearChecker % 4 == 0:
        if yearChecker % 100 == 0 and yearChecker % 400 == 0:
            break
        elif yearChecker % 400 != 0 and yearChecker % 100 == 0:
            yearChecker += 1
        else:
            break
    else:
        yearChecker += 1
print(f"The next leap year after {year} is {yearChecker}")


