from pprint import pprint
import random

#1 - Create Car class with properties, iniatialise 
class Car:
    def __init__(self, regNumber, maxSpeed, currentSpeed = 0, distanceTravelled = 0):
        self.regNumber = regNumber
        self.maxSpeed = maxSpeed
        self.currentSpeed = currentSpeed
        self.distanceTravelled = distanceTravelled

firstCar = Car("ABC-123", 142)
#print(f"Registration: {firstCar.regNumber}\nMax speed: {firstCar.maxSpeed}\nCurrent speed: {firstCar.currentSpeed}\nDistance travelled: {firstCar.distanceTravelled}")
pprint(vars(firstCar))      #easy method to print all variables of a class

# 2 - First class but with new method.
class Car:

    currentSpeed = 0
    distanceTravelled = 0

    def __init__(self, regNumber, maxSpeed):
        self.regNumber = regNumber
        self.maxSpeed = maxSpeed

    def accelerate(self, changeOfSpeed):
        if changeOfSpeed > 0:
            if self.currentSpeed + changeOfSpeed < self.maxSpeed:
                self.currentSpeed += int(changeOfSpeed)
            else:
                self.currentSpeed = self.maxSpeed
        if changeOfSpeed < 0:
            if self.currentSpeed + changeOfSpeed <= 0:      #using + because change of speed is negative
                self.currentSpeed = 0
            else:
                self.currentSpeed -= changeOfSpeed

firstCar = Car("ABC-123", 142)

#3 ways of displaying information 
#print(f"Registration: {firstCar.regNumber}\nMax speed: {firstCar.maxSpeed}\nCurrent speed: {firstCar.currentSpeed}\nDistance travelled: {firstCar.distanceTravelled}")
#print(firstCar.regNumber, firstCar.maxSpeed, firstCar.currentSpeed, firstCar.distanceTravelled)
#pprint(vars(firstCar))

print(firstCar.currentSpeed)    #speed = 0
firstCar.accelerate(30)
print(firstCar.currentSpeed)    #speed = 30
firstCar.accelerate(70)
print(firstCar.currentSpeed)    #speed = 100
firstCar.accelerate(50)
print(firstCar.currentSpeed)    #speed is capped at 142
firstCar.accelerate(-200)
print(firstCar.currentSpeed)    #speed is reduced to lowest speed of 0


# 3 Extended again to add a drive method within the class
class Car:

    currentSpeed = 0
    distanceTravelled = 0

    def __init__(self, regNumber, maxSpeed):
        self.regNumber = regNumber
        self.maxSpeed = maxSpeed

    def accelerate(self, changeOfSpeed):
        if changeOfSpeed > 0:
            if self.currentSpeed + changeOfSpeed < self.maxSpeed:
                self.currentSpeed += int(changeOfSpeed)
            else:
                self.currentSpeed = self.maxSpeed
        if changeOfSpeed < 0:
            if self.currentSpeed + changeOfSpeed <= 0:      #using + because change of speed is negative
                self.currentSpeed = 0
            else:
                self.currentSpeed -= changeOfSpeed

    def drive(self, hours):
        self.distanceTravelled += self.currentSpeed * hours

firstCar = Car("ABC-123", 142)
firstCar.distanceTravelled = 2000   #sets distance travelled to 2000
firstCar.accelerate(60)             #sets current speed to 60
firstCar.drive(1.5)                 #travels for 1.5 hours
print(firstCar.distanceTravelled)   #displays distance = 2090


#4 - Car race 
class Car:
    def __init__(self, regNumber, maxSpeed):
        self.regNumber = regNumber
        self.maxSpeed = maxSpeed
        self.currentSpeed = 0
        self.distanceTravelled = 0

    def accelerate(self, changeOfSpeed):
        if changeOfSpeed > 0: # and change + current < maxspeed -> equal this + that, else = maxspeed
            if (self.currentSpeed + changeOfSpeed) <= self.maxSpeed:
                self.currentSpeed += int(changeOfSpeed)
            else:
                self.currentSpeed = self.maxSpeed
        if changeOfSpeed < 0:
            if (self.currentSpeed + changeOfSpeed) <= 0:      #using + because change of speed is negative
                self.currentSpeed = 0
            else:
                self.currentSpeed -= changeOfSpeed

    def drive(self, hours):
        self.distanceTravelled += self.currentSpeed * hours

carList = []

#this creates 10 cars and adds them to the list 
for x in range(0,10):
    newCar = Car("ABC-" + str(x + 1), random.randint(100, 200))
    carList.append(newCar)
    
#10k km finishes the race, every hour speed is updated (-10, +15 km/h)
raceOn = True
while raceOn:                                               #to run code until desired outcome
    for car in range(len(carList)):                         #to go through every car to drive and accelerate
        carList[car].drive(1)                               #car drives for 1 hour 
        if carList[car].distanceTravelled >= 1000:          #if current car finished then race is over
            print(carList[car].regNumber + " won!")
            raceOn = False                                  #Stops race and other cars from moving if someone got to the finish line first
            break                                           #poor wording in question because not all cars get to drive for the final hour
        else:
            carList[car].accelerate(random.randint(-10, 15))

print("The stats are as follows:")
for x in range(len(carList)):
    print("Registration number: " + str(carList[x].regNumber) + ", Distance travelled: " + str(carList[x].distanceTravelled))
