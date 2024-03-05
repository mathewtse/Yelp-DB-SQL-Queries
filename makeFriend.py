# Make Friend 

def makeFriendFunction(cursor, conn, currentUserID):

    # get user input for the friendID
    correctFriendID = False 
    while(correctFriendID == False):
        friendID = input("Please enter the userID that you would like to become friends with: ").strip()
        # check if the friendID exists in the database
        cursor.execute('SELECT user_id FROM user_yelp WHERE user_id = ' + "'" + friendID + "'")
        row = cursor.fetchone()
        if(row != None and row[0] == friendID and friendID != currentUserID):
            correctFriendID = True
        else:
            print("Sorry, that is an invalid friend ID. Please Try again.")
    
    # insert the friend into the database

    insertFriendship = 'INSERT INTO friendship(user_id, friend) VALUES(?,?)'
    cursor.execute(insertFriendship, currentUserID, friendID)
    conn.commit()
    if(cursor.rowcount != 0):
        print("Friend successfully made!")