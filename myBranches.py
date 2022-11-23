from email import message
from github import Github
from prettytable import PrettyTable
import mysql.connector
table = PrettyTable()
table.field_names = ["Repository Name", "Branches", "Commits"]

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

    branches=[]
    list_branches = list(repository.get_branches())
    for branche in list_branches:
        branches.append(branche.name)
        sql = " INSERT INTO branche( nameBranche ,nameRepo ) VALUES (%s, %s)"
        
        val = (branche.name,name)
        mycursor.execute(sql, val)
        print(mycursor.rowcount, "record inserted.")
        mydb.commit()
       
    commits=""
    try:
        list_commits = list(repository.get_commits())
        for commit in list_commits:
            commits += commit.commit.message + "\n"
            sql = " INSERT INTO commit ( nameRepo ,message,createdat ) VALUES (%s, %s,%s)"
            val = (repository.name,commit.commit.message,commit.author.created_at)
            mycursor.execute(sql, val)
            print(mycursor.rowcount, "record inserted.")
            mydb.commit()
    except:
        print("empty branche")
        table.add_row([name,  str(branches), commits ])

print(table)
