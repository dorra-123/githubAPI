from github import Github

#generated access token
access_token ="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"

#login into github account
#login  = Github(access_token)

# using username and password
login = Github("dorra-123", access_token)

#get the user
user  = login.get_user()

repository_name= "Dorra-Repo-3"

#create repository
new_repo = user.create_repo(repository_name)

#create new file
new_repo.create_file("New-File.txt", "new commit", "Data Inside the File")