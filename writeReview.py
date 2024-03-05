# Write Review

import random
import string
from datetime import datetime

EMPTY = 'empty'
INTEGER = 'integer'
INVALID = 'invalid'

def checkInputType(input):
    if(input == ''): # if empty string, return EMPTY
        return EMPTY
    try: # try converting to an integer 
        val = int(input)
        # return NUMBER if the float is within bounds
        if(val >= 1 and val <= 5):
            return INTEGER
        else:
            print("Please enter an integer between 1 and 5")
            return INVALID 
    except ValueError: # if input cannot be converted to an integer, then it must be a float or string
        print("Please enter an integer between 1 and 5") 
        return INVALID 

def writeReviewFunction(cursor, conn, currentUserID):

    # get the business ID 
    print("Welcome to write a review!")

    correctBusinessID = False 
    businessID = ''
    while(correctBusinessID == False):
        businessID = input("Please enter the Business ID that you would like to write a review for: ").strip()
        # check if the business ID exists in the database
        cursor.execute('SELECT business_id FROM business WHERE business_id = ' + "'" + businessID + "'")
        row = cursor.fetchone()
        if(row != None and row[0] == businessID):
            correctBusinessID = True
        else:
            print("Sorry, that is an invalid Business ID. Please Try again.")
    
    # get the number of stars 
    numberOfStars = ''
    numberOfStarsInputType = EMPTY

    while(numberOfStarsInputType != INTEGER):
        numberOfStars = input("Please enter the number of stars between 1 and 5 as an INTEGER: ")
        numberOfStarsInputType = checkInputType(numberOfStars)

    # generate the random review ID 
    correctReviewID = False
    reviewID = ''
    while(not correctReviewID):
        reviewID = (''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=22)))
        # check that the review ID does not exist in the database
        cursor.execute('SELECT review_id FROM review WHERE review_id = ' + "'" + reviewID + "'")
        row = cursor.fetchone()
        if(row == None):
            correctReviewID = True 
    
    # generate the current date and time 
    now = datetime.now()
    date = now.date()
    time = now.time().isoformat(timespec='milliseconds')
    dateandtime = str(date) + " " + str(time) 

    # insert into the database 
    insertReview = 'INSERT INTO review(review_id, user_id, business_id, stars, useful, funny, cool, date) VALUES(?,?,?,?,0,0,0,?)'
    cursor.execute(insertReview, reviewID, currentUserID, businessID, numberOfStars, dateandtime)
    conn.commit()
    if(cursor.rowcount != 0):
        print("Review Successfully added!")