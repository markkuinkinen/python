import pprint
import random

# Exercise 1: Create an elevator class that takes top/bottom floor as parameters and move elevators between floors
class Elevator:
    def __init__(self, bottomFloor, topFloor):
        self.bottomFloor = bottomFloor
        self.topFloor = topFloor
        self.currentFloor = bottomFloor

    def floorUp(self):
        if (self.currentFloor + 1) < self.topFloor:
            self.currentFloor += 1
            print(f"On floor {self.currentFloor}")

    def floorDown(self):
        if (self.currentFloor - 1) >= self.bottomFloor:
            self.currentFloor -= 1
            print(f"On floor {self.currentFloor}")

    def go_to_floor(self, floor):
        if (floor >= self.bottomFloor and floor > self.currentFloor and floor < self.topFloor):
            while self.currentFloor != floor:
                self.floorUp()
        elif (floor <= self.topFloor and floor < self.currentFloor and floor > self.bottomFloor):
            while self.currentFloor != floor:
                self.floorDown()
        else:
            if (floor == self.currentFloor):
                print("You are already on this floor")
            else:
                print(f"You are currently on {self.currentFloor} attempting to go to floor {floor}. The bottom/top floors are {self.bottomFloor}/{self.topFloor}")

firstElevator = Elevator(2, 10)

print(f"Current floor: {firstElevator.currentFloor}, bottom floor: {firstElevator.bottomFloor}, top floor: {firstElevator.topFloor}")

firstElevator.go_to_floor(6)
firstElevator.go_to_floor(10)
firstElevator.go_to_floor(6)
firstElevator.go_to_floor(3)
firstElevator.go_to_floor(-1)

print(f"Current floor: {firstElevator.currentFloor}, bottom floor: {firstElevator.bottomFloor}, top floor: {firstElevator.topFloor}")

# Exercise 2 - Extend elevator class by creating building class, elevators go in buildings
class Elevator:
    def __init__(self, bottomFloor, topFloor):
        self.bottomFloor = bottomFloor
        self.topFloor = topFloor
        self.currentFloor = bottomFloor

    def floorUp(self):
        if (self.currentFloor + 1) <= self.topFloor:
            self.currentFloor += 1
            print(f"On floor {self.currentFloor}")

    def floorDown(self):
        if (self.currentFloor - 1) >= self.bottomFloor:
            self.currentFloor -= 1
            print(f"On floor {self.currentFloor}")

    def go_to_floor(self, floor):
        if (floor >= self.bottomFloor and floor > self.currentFloor and floor <= self.topFloor):
            while self.currentFloor != floor:
                self.floorUp()
        elif (floor <= self.topFloor and floor < self.currentFloor and floor >= self.bottomFloor):
            while self.currentFloor != floor:
                self.floorDown()
        else:
            if (floor == self.currentFloor):
                print("You are already on this floor")
            else:
                print(f"You are currently on {self.currentFloor} attempting to go to floor {floor}. The bottom/top floors are {self.bottomFloor}/{self.topFloor}")

class Building:
    def __init__(self, numOfElevators, bottomFloor, topFloor):
        self.eList = []
        for i in range(numOfElevators):
            newElevator = Elevator(bottomFloor, topFloor)
            self.eList.append(newElevator)
        
    def run_elevator(self, ele_num, destination_floor):
        if (ele_num >= 0 and ele_num < len(self.eList)):
            self.eList[ele_num].go_to_floor(destination_floor)
        else:
            print("That elevator does not exist")

      # Exercise 3 add-on
    def fire_alarm(self):
        for i in range(len(self.eList)):
            self.eList[i].go_to_floor(self.eList[i].bottomFloor)
            print(f"Elevator: {i} is now at floor {self.eList[i].bottomFloor}")

apartment = Building(3, 1, 6)
apartment.run_elevator(0, 6)
apartment.run_elevator(1, 4)
apartment.run_elevator(2, 3)

apartment.fire_alarm()

print(apartment.eList[0].bottomFloor)

# Exercise 4 

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
                self.currentSpeed += changeOfSpeed

    def drive(self, hours):
        self.distanceTravelled += self.currentSpeed * hours

class Race:
    def __init__(self, name, distance, carList):
        self.raceName = name
        self.raceDistance = distance
        self.carList = carList      
        self.timer = 0

    def hour_passes(self):
        for cars in range(len(carList)):
            carList[cars].drive(1)
            carList[cars].accelerate(random.randint(-10, 15))
            if cars == 9: #len(carList):
                self.timer += 1
            if self.timer % 10 == 0:
                print(f"{self.timer} hour/s has passed")
                self.print_status()

    def print_status(self):
        for cars in range(len(carList)):
            print(f"Car: {carList[cars].regNumber}  -  Max speed: {carList[cars].maxSpeed}  -  Distance travelled: {carList[cars].distanceTravelled}")

    def race_finished(self):
        for cars in range(len(carList)):
            if (carList[cars]).distanceTravelled >= self.raceDistance:
                print(f"\n\n{carList[cars].regNumber} won!")
                self.print_status()
                return True

carList = []

#this creates 10 cars and adds them to the list 
for x in range(0,10):
    newCar = Car("ABC-" + str(x + 1), random.randint(100, 200))
    carList.append(newCar)

GDDrace = Race("Grand Demolition Derby", 8000, carList)

while not GDDrace.race_finished():
    GDDrace.hour_passes()
    print(GDDrace.timer)