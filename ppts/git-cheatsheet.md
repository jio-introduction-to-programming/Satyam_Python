# Simple Git Cheatsheet


1. `git init`: Initializes a new Git repository in the current directory.
 - Example: `git init` creates a new empty repository to track your project.

2. `git clone <repository>`: Copies an existing repository from a remote source to your local machine.
 - Example: `git clone https://github.com/user/repo.git` downloads the repository to your computer.

3. `git add <file>`: Adds changes in a file to the staging area for the next commit.
 - Example: 

```
git add myfile.py # Stages changes made in myfile.py
git add . # Stages all changes in the current directory
```

4. `git commit -m "<message>"`: Records changes to the repository with a descriptive message.
 - Example: 
```
git commit -m "Add new feature"
```
saves the staged changes with the message "Add new feature."

5. `git status`: Displays the current status of the repository, including modified files and untracked files.

 - Example: 
```
git status
```
shows the list of files that have been modified or added to the repository.


6. `git log`: Shows a history of commits in the repository, including commit messages and authors.
 - Example: 
```
git log
```
displays a chronological list of commits made in the repository.

7. `git branch`: Lists all branches in the repository.
 - Example: 
```
git branch # Lists all branches
git branch feature # Creates a new branch named "feature"
```

8. `git checkout <branch>`: Switches to a different branch in the repository.

 - Example: 
```
git checkout feature-branch
```
 changes to the branch named "feature-branch."

9. `git pull`: Updates your local repository with the latest changes from the remote repository.
 - Example: 
```
git pull
```
fetches and merges the latest changes from the remote repository into your local repository.

10. `git push`: Sends your local commits to the remote repository.

 - Example: 
```
git push
```
 uploads your committed changes to the remote repository.

11. `git config user.name <name>`: Sets the name associated with your Git commits.
 - Example:
``` 
git config user.name "John Doe"
```
 sets the name to "John Doe" for your commits.

12. `git config user.email <email>`: Sets the email associated with your Git commits.
 - Example: 
```
git config user.email "john.doe@example.com"` 
```
sets the email to "john.doe@example.com" for your commits.

13. `git stash`: Temporarily saves changes that are not ready to be committed.
 - Example:
```
git stash # Stashes the changes
git stash apply # Applies the stashed changes back to the working directory
```

14. `git remote -v`: Shows the remote repository's URL.
 - Example: 
```
git remote -v
```
displays the URLs for the remote repository.

15. `git remote set-url origin <new-url>`: Sets a new URL for the remote repository named "origin."
 - Example: 
```
git remote set-url origin https://github.com/user/repo.git
```
updates the URL of the remote repository.