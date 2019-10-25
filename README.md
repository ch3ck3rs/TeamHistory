# TeamHistory

### Source paths should be kept in the source file.  
This will allow us to have an LVsource and a GarrettSource file with seperate local paths

### Using git
If you are not a fan of the git bash command style interface, PyCharm will do just about all of it for you.

The basics of git are: pull > add > commit > push
- Repository (or repo) 
    - this is what sits on github.com
    - it holds all the master files and is like the back up
- pull (a fresh copy of the repo if changes were made by someone else)
- add (file(s) that you want to track)
- commit (changes, this creates a refresh point)
- push (changes back to the repo so others can see them)
- **_until you commit and push_** no changes can be seen by others

- notes
    - you must add a file every time you make a change to it
        - or just wait til you want to commit, then pull > add --all > commit > push 
    - git status (in the terminal will show you which files are ready to be committed, which are being tracked but will
    not be committed right not, and those which are not tracked)
    - PyCharm > Version Control > Default Change list will also tell you this
        - green - edited since last commit and ready for next commit (git add was done since your last edit)
        - blue - edited since last commit but will not be committed (you have made a change since the last git add)
        - red - not being tracked, have never done git add
        - white - tracked but no edits since last commit

#### git branching
You can create a new branch of the project, play around with it, pull in updates from the master branch, make commits 
and push to the repo without affecting the main program (like a sandbox).  When you get the new feature working on your 
branch, it can then be merged back into the master.
   