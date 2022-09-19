
#1 Checks if a fish is too small to catch
cm = float(input("Enter the length of the zander in cm: "))
if (cm < 42):
    print("You best be throwing that zander back! It is " + (str(42-cm)) + " cm too short!")
else:
    print("Enjoy the appropriately sized zander!")


#2  Cabin class checker
cabinClass = str(input("Enter your cabin class (LUX, A, B, C) for this cruise: "))
if cabinClass == "A" or cabinClass == "a":
    print("Above the car deck, equipped with a window.")
elif cabinClass == "B" or cabinClass == "b":
    print("Windowless cabin above the car deck.")
elif cabinClass == "C" or cabinClass == "c":
    print("Windowless cabin below the car deck.")
elif cabinClass == "LUX" or cabinClass == "Lux" or cabinClass == "lux":
    print("Upper deck cabin with a balcony.")
else:
    print("Invalid cabin class.")


#3 Checks hemoglobin level 
gender = str(input("Enter is your biological gender (F/M): "))
if gender == "f" or gender == "F":
    hemoLevel = int(input("Enter is your hemoglobin value (g/l): "))
    if hemoLevel < 117:
        print("Your hemoglobin level is low.")
    elif hemoLevel >= 117 and hemoLevel <= 155:
        print("Your hemoglobin level is normal.")
    elif hemoLevel > 155:
        print("Your hemoglobin level is high")
    else:
        print("Invalid value entered.")
elif gender == "m" or gender == "M":
    hemoLevel = int(input("Enter is your hemoglobin value (g/l): "))
    if hemoLevel < 134:
        print("Your hemoglobin level is low.")
    elif hemoLevel >= 134 and hemoLevel <= 167:
        print("Your hemoglobin level is normal.")
    elif hemoLevel > 167:
        print("Your hemoglobin level is high")
    else:
        print("Invalid value entered.")
else:
    print("Invalid gender entered.")


#4 leap year checker
year = int(input("Enter a year to find out if it's a leap year: "))
if year % 100 == 0 and year % 400 == 0:
    print("It's a leap year.")
elif year % 4 == 0:
    print("It's a leap year.")
else:
    print("It's not a leap year.")