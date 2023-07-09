# %%
# Developer: seungwan_ryu
# Date: 2023.07.02
# Contents: git hub test

print("Hello, world")
print("We will start git-hub. We can do it.")
print("Hey big brothers, Let's do it together.")

# %%

### initialize and start a git
# git init

### Setting account information
# git config -global user.name "name"
# git config -global user.email "xxxx@xxxxx.com"

### confirm a config list 
# git config --list

### current state
# git status

### adding files to the staging area
# git add . # whole files

### commit
# git commit -m "xxxx"
# git commit -m "xxxx" --amend # revise the commit

### confirm the commit logs
# git log

### connect between local and remote
# git remote add origin [git hub adress]

### confirm the current configured remote repository
# git remote -v

### push the local soruce to the remote repository
# git push origin master
# git push origin [new_branch] # create a new_branch in remote repository and push

### create a branch
# git branch [name]

### move to the branch
# git checkout [name]
# git checkout -b [name] # create a branch and move to the branch simultaneously

### delete the branch
# git branch -d [name]

### pull the code of the master of the remote
# git pull origin master