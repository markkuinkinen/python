

#1 Asks user for number of month, displays season (Tuple) - like list but static, can't be changed
seasons = ("Spring", "Summer", "Autumn", "Winter")
while True:
    userinput = input("Enter the number of a month to see what season it is: ")
    if (userinput == ""):
        print("Exiting")
        break
    monthNumber = int(userinput)
    if monthNumber > 2 and monthNumber < 6:
        #print("The season is: " + str(seasons[0]))
        print(f"The season is: {seasons[0]}")
    elif monthNumber > 5 and monthNumber < 9:
        print("The season in: " + str(seasons[1]))
    elif monthNumber > 8 and monthNumber < 12:
        print("The season is: " + str(seasons[2]))
    elif (monthNumber > 0 and monthNumber < 3) or monthNumber == 12:
        print("The season is: " + str(seasons[3]))
    else:
        print("Invalid month")


#2 Asks user to input names, prints "new" or "existing" depending. {set} shit list, unordered, can't be indexed, cant have multiple
inputNames = set()
while True:
    nameToCheck = str.lower(input("Enter a name: "))
    if nameToCheck == "":   #this stops the code
        for amount in inputNames:   #prints the contents of set 
            print("The set contains name: " + amount)
        break
    
    nameToCompare = nameToCheck in inputNames    #nameToCompare returns true if nameToCheck is in inputNames
    if nameToCompare:
        print("Already exists")
    else:
        print("New name, adding to set")
        inputNames.add(nameToCheck)


# 3 Dictionary - Add to existing dictionary, find key or value based on either one.
airports = {"EFHK":"Helsinki-Vantaa",   #code = key, value = airportname
            "YSSY":"Sydney Airport"}
while True:
    request = input("Enter int for what you would like to do:\n1. Enter airport\n2. Fetch airport information\n3. Quit\nOption: ")
    if request == "1":
        enteredCode = input("Enter an ICAO code: ")
        enteredAirport = input("Enter an Airport name: ")
        print("Airport information has been added.\n")
        airports[enteredCode] = enteredAirport      #makes new key in airports dictionary (ICAO code) and sets the value (airport name)
        #print("Airport information has been added.\n")
    elif request == "2":
        code = str(input("Enter the airport's ICAO code or Name: "))
        if code in airports:
            print(f"Airport name: {airports[code]}")     #uses the code (which is the key) to print the value of the code
        for key, value in airports.items():     #checks if input == value (airport name) and prints it
            if code == value:
                print(f"The airport key: {key}")
    elif request == "3":
        print(airports)
        break
    else:
        print("Error: Enter a number between 1-3")


