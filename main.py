# Created by Mathew Tse

import pyodbc
import login 
import searchbusiness 
import searchUsers
import makeFriend
import writeReview

# connecting to the Database 

conn = pyodbc.connect('driver={SQL Server};server=cypress.csil.sfu.ca;uid=s_mta118;pwd=dYhRTaqrmREN7Fa2')
cur = conn.cursor()
cur.execute( 'SELECT username from dbo.helpdesk' )
row = cur.fetchone()
while row:
    print ( 'SQL Server standard login name = ' + row [ 0 ] )
    row = cur.fetchone()

# login
user_id = login.loginFunction(cur)

# main menu
continueRunning = True 
while(continueRunning):

    print("What would you like to do?")
    print("Enter 1 for Search Business")
    print("Enter 2 for Search Users")
    print("Enter 3 for Make Friend")
    print("Enter 4 for Write Review")
    print("Enter 5 to Exit")

    usersChoice = input("Please enter one of the options above: ").strip()

    if(usersChoice == "1"):
        searchbusiness.searchBusinessFunction(cur)
    elif(usersChoice == "2"):
        searchUsers.searchUsersFunction(cur)
    elif(usersChoice == "3"):
        makeFriend.makeFriendFunction(cur, conn, user_id)
    elif(usersChoice == "4"):
        writeReview.writeReviewFunction(cur, conn, user_id)
    elif(usersChoice == "5"):
        continueRunning = False
    else:
        print("Sorry, you did not type in type in a valid option. Please try again.")

conn.close()