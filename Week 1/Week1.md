  **BYTEWISE ML/DL Track**
  
  **WEEK 1**
  

**GIT:**

      - Git is a version control system.
      
      - Git helps you keep track of code changes.
      
      - Git is used to collaborate on code.

**GIT HUB:**

      - GitHub is a "hub" (a place or platform) where Git users build software together. 
        GitHub is also an hosting provider and version control platform you can use to 
        collaborate on open source projects and share files. 
        When you're using GitHub, you're working with Git beneath the hood.


* Install Git
* Check version

                git --version
* configure username and email for git
* Create a directory and initiliaze it in git

                git init
* Now we have a git repository (but its empty)
* Add some files to the directory and "add" them to the staging environment (not yet "commited")
  
                git add idk.md
                git add -all     or     git add -A
* Now we commit (commit is like saving)

                git commit -m "Some message you should write"
* The staging step is skippable yet not recommended
* Now check the log

                git log
* Branch are a separate version of the prject where doing changings do not effect the orignal project

                git branch idk-sm-branch-name
* we need to move to that branch now so:

                git checkout idk-sm-branch-name
* Make changes, "add" and then "commit" it
* we can go back to master and make another branch were we fix some other issue
* Now we need to merge the branch with master so first go to master

                git merge emergency-fix
* now delete the branch emergency-fix since there is no longer any use

                git branch -d emergency-fix
