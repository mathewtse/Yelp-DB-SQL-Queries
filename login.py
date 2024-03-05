# Login 

def loginFunction(cursor): 

    loggedIn = False

    while(loggedIn == False):
        loginInput = str(input('Please enter your user id: '))
        cursor.execute("SELECT COUNT(1) FROM user_yelp WHERE user_id = ?", (loginInput,))
        loginResult = cursor.fetchone()[0]

        if(loginResult == 1):
            loggedIn = True
            print("You have successfully logged in!\n")
        else:
            print("Sorry, the user id entered was invalid.\n")
            loggedIn = False

    return loginInput 