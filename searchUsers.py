# Search Users

EMPTY = 'empty'
INVALID = 'invalid'
YESORNO = 'yesorno'

def checkInputType(input):
    if(input == ''): # if empty string, return EMPTY
        return EMPTY
    elif(input == 'yes' or input == 'no'):
        return YESORNO
    else:
        return INVALID

def searchUsersFunction(cursor):
    print("Welcome to the search users function!")

    # get user input for name 
    nameInput = input("Please enter the name of the user you would like to search\nLeave blank and press enter if you would like to skip: ").strip()
    
    # get user input for useful
    usefulInput = '' 
    usefulInputType = INVALID
    while(usefulInputType == INVALID):
        usefulInput = input("Please enter yes or no for searching by useful:\nLeave blank and press enter if you would like to skip: ").strip().lower()
        usefulInputType = checkInputType(usefulInput)

    # get user input for funny
    funnyInput = ''
    funnyInputType = INVALID
    while(funnyInputType == INVALID):
        funnyInput = input("Please enter yes or no for searching by funny:\nLeave blank and press enter if you would like to skip: ").strip().lower()
        funnyInputType = checkInputType(funnyInput)

    # get user input for cool
    coolInput = ''
    coolInputType = INVALID
    while(coolInputType == INVALID):
        coolInput = input("Please enter yes or no for searching by cool:\nLeave blank and press enter if you would like to skip: ").strip().lower()
        coolInputType = checkInputType(coolInput)

    numOfFilters = 0
    whereString = ' WHERE'

    if(nameInput != ''):
        whereString += ' name LIKE ' + "'%" + nameInput + "%'"
        numOfFilters += 1

    if(usefulInputType == YESORNO):
        if(numOfFilters >= 1):
            whereString += ' AND'
        if(usefulInput == 'yes'):
            whereString += ' useful >= 1'
        elif(usefulInput == 'no'):
            whereString += ' useful = 0'
        numOfFilters += 1

    if(funnyInputType == YESORNO):
        if(numOfFilters >= 1):
            whereString += ' AND'
        if(funnyInput == 'yes'):
            whereString += ' funny >= 1'
        elif(funnyInput == 'no'):
            whereString += ' funny = 0'
        numOfFilters += 1

    if(coolInputType == YESORNO):
        if(numOfFilters >= 1):
            whereString += ' AND'
        if(coolInput == 'yes'):
            whereString += ' cool >= 1'
        elif(coolInput == 'no'):
            whereString += ' cool = 0'
        numOfFilters += 1
    
    if(numOfFilters == 0):
        whereString = ''

    # create and execute the sql statement
    sqlString = "SELECT user_id, name, useful, funny, cool, yelping_since FROM user_yelp" + whereString + " ORDER BY name"
    cursor.execute(sqlString)
    row = cursor.fetchone()
    if(row == None):
        print("No Results!")
    while row:
        useful = float(row[2])
        funny = float(row[3])
        cool = float(row[4])

        if(useful >= 1):
            useful = 'Yes'
        else:
            useful = 'No'
        if(funny >= 1):
            funny = 'Yes'
        else:
            funny = 'No'
        if(cool >= 1):
            cool = 'Yes'
        else:
            cool = 'No'

        print("User ID: " + str(row [0]) + " | Name: " + str(row[1]) + " | Useful: " + useful + " | Funny: " + funny + " | Cool: " + cool + " | Yelping Since: " + str(row[5]))
        row = cursor.fetchone()