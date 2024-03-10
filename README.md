# Yelp-DB-SQL-Queries

A command line program that enables the user to interact with a Yelp Database
Created using Python with the pyodbc module, and Microsoft SQL Server


**Functionality:**

**1) Log in**
- When the user first runs the program, they are asked to enter their userID
- An SQL Query is run. If the userID is found in the database, they can proceed with using the other features of the program
- If the userID is not found in the database, then they must enter their userID again

--- Once the user has logged in, they have access to the below features:

**2) Search for a Business**
- The user is able to search for a business
- Search criteria include: name (or part of a name), minimum and maximum number of stars, and city
- After the search is complete, a list of businesses is displayed on the command line

**3) Search for a User**
- The user can search for another user
- Search criteria include: name (or part of their name), useful (yes/no), funny (yes/no), cool (yes/no)
- After the search is complete, a list of users is displayed on the command line

**4) Make Friend**
- The user can enter a userID that they would like to be friends with
- The friendship is recorded in the Friendship Table

**5) Write Review**
- The user can write a review for a business
- The user enters the businessID and provides the number of stars
- The review is appended to the Review Table
- The program automatically updates the number of stars the review count for the business using Triggers implemented in the SQL Database
