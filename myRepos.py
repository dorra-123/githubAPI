from github import Github
from prettytable import PrettyTable
import mysql.connector

#create an empty pretty table 
table = PrettyTable()

#create a header for our pretty table with 5 columns names
table.field_names = ["Repository Name", "Private", "Public","Created Date","Language"]

#github generated access token (to communicate securely with github)
access_token ="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"

#login with access token
login  = Github("dorra-123", access_token)

#get the user
user  = login.get_user()

#get all repositories
my_repos = user.get_repos()

# connect to database
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="git"
)
#create a cursor
mycursor = mydb.cursor()

#loop in my repos to get data for each repository 
for repository  in my_repos:
    #get data for each repository 
    name =  repository.name
    private,public = repository.private, not(repository.private)
    created_date = repository.created_at
    language = repository.language

    #add row for each repository in the pretty table 
    table.add_row([name, private, public, created_date, language])

    #save data in database 
    try:
        #prepare sql request 
        sql = " INSERT INTO repository ( name , private ,  public , createddate, language) VALUES (%s, %s,%s,%s,%s)"
        #set values for different columns 
        val = (name, private, public, created_date, language)
        #execute sql request 
        mycursor.execute(sql, val)
        #commit change 
        mydb.commit()
        #show success message 
        print(mycursor.rowcount, "record inserted.")
    except:
        #catch error in failure case such as data already exists 
        print("data already exists")
#print table 
print(table)