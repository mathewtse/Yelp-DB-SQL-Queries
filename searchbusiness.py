# Search Business Function

EMPTY = 'empty'
NUMBER = 'number'
INVALID = 'invalid'

def checkInputType(input):
    if(input == ''): # if empty string, return EMPTY
        return EMPTY
    try: # try converting to a float 
        val = float(input)
        # return NUMBER if the float is within bounds
        if(val >= 0 and val <= 5):
            return NUMBER
        else:
            return INVALID 
    except ValueError: # if input cannot be converted to a float, then it must be a string 
        return INVALID 

def searchBusinessFunction(cursor):
    print("Welcome to the Search Business Feature!")

    # get user input for the minimum number of stars
    minNumOfStarsInputtedType = INVALID
    minNumOfStars = ''
    # keep getting input from user until it is valid 
    while(minNumOfStarsInputtedType == INVALID):
        minNumOfStars = input("Please enter the minimum number of stars between 0 and 5: (Leave blank and press enter if you would like to skip) ").strip()
        minNumOfStarsInputtedType = checkInputType(minNumOfStars)

    # get user input for the maximum number of stars 
    maxNumOfStarsInputtedType = INVALID
    maxNumOfStars = ''
    # keep getting input from the user until it is valid 
    while(maxNumOfStarsInputtedType == INVALID):
        maxNumOfStars = input("Please enter the maximum number of stars between 0 and 5: (Leave blank and press enter if you would like to skip) ").strip()
        maxNumOfStarsInputtedType = checkInputType(maxNumOfStars)
        if(maxNumOfStarsInputtedType != EMPTY and maxNumOfStarsInputtedType != INVALID and minNumOfStarsInputtedType != EMPTY):
            if(maxNumOfStars < minNumOfStars):
                maxNumOfStarsInputtedType = INVALID
                print("Maximum number of stars inputted must be greater or equal to the minimum number of stars inputted. ")

    cityName = input("Please enter the city name: (Leave blank and press enter if you would like to skip) ").strip().lower().capitalize()
    name = input("Please enter the business name or part of the business name: (Leave blank and press enter if you would like to skip) ").strip().lower().capitalize()
    
    numOfFilters = 0
    whereString = ' WHERE'

    if(minNumOfStarsInputtedType == NUMBER):
        whereString += ' stars >= ' + minNumOfStars
        numOfFilters += 1

    if(maxNumOfStarsInputtedType == NUMBER):
        if(numOfFilters >= 1):
            whereString += ' AND stars <= ' + maxNumOfStars
        else:
            whereString += ' stars <= ' + maxNumOfStars
        numOfFilters += 1

    if(cityName != ''):
        if(numOfFilters >= 1):
            whereString += ' AND city = ' + "'" + cityName + "'"
        else:
            whereString += ' city = ' + "'" + cityName + "'"
        numOfFilters += 1

    if(name != ''):
        if(numOfFilters >= 1):
            whereString += ' AND name LIKE ' +  "'%" + name + "%'"
        else:
            whereString += ' name LIKE ' + "'%" + name + "%'" 
        numOfFilters += 1
    
    if(numOfFilters == 0):
        whereString = ''

    sqlString = "SELECT business_id, name, address, city, stars FROM business" + whereString
    cursor.execute(sqlString)

    row = cursor.fetchone() 
    if(row == None):
        print("No Results!")
    while row:
        print ("Business ID: " + str(row [0]) + " | Name: " + str(row[1]) + " | Address: " + str(row[2]) + " | City: " + str(row[3]) + " | Number of Stars: " + str(row[4]))
        row = cursor.fetchone()