from github import Github
from prettytable import PrettyTable
import mysql.connector
table = PrettyTable()
table.field_names = ["Repository Name", "Commits"]
#github generated access token
access_token ="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"

#login with access token
login  = Github("dorra-123", access_token)
#get the user
user  = login.get_user()

#get all repositories
my_repos = user.get_repos()
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="git"
)
mycursor = mydb.cursor()

for repository  in my_repos:
    name =  repository.name
        
    commits=""
    try:
        list_commits = list(repository.get_commits('main'))

        for commit in list_commits:
            commits += commit.commit.message + "\n"
            

             
    except:
        print("empty repo")

    table.add_row([repository.name,  commits ])
     
print(table)
