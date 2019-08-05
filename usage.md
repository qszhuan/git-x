# Usage
## git x
Here are the available commands:
```
a	Add file contents to the index
amend	Amend files into repository
b	Show current branch name
ci	Commit all the indexed files
cia	Add files into index and commit
co	Checkout/Create branch
llg	Show recent <number> logs
m	Merge codes from branch <from> to current branch
p	Pull latest code
pr	Create pull request from current branch to <to_branch>
st	Show the working tree status
up	Create remote branch
```
## git a
The usage is:
```

Add file that specified in <pathspec> contents into the index.
Ignore/Remove the file contents from the index if the files are specified in the -x option.
The <pathspec> syntax is same as the one in 'git status' parameter.

Examples:
    1. Add all sql files:
        git a *.sql
    2. Add all files, but ignore all config files(ending with .config extensions)
        git a . -x *.config
    3. Ignore multiple files(*.config, *.md) by using more than one '-x' to specify multiple patterns.
        git a . -x *.config -x *.md
    4. Remove all config files from the index
        git -x *.config
```
## git amend
The usage is:
```

Amend files into repository, this only amend the files that already in the index.

Examples:
    1. Amend without editing
        git amend
    2. Amend, and edit the commit message, this will open the editing window,
        depends on what editor is configured in git.
        git amend -e
```
## git b
The usage is:
```

Show current branch name.

Example:
    git b
```
## git ci
The usage is:
```

Commit all the indexed files into repository, same as 'git commit -m <comment>'.

Example:
    git ci "This is the comment."
```
## git cia
The usage is:
```

Add content files into index, and then create a new commit.
By default it will add all the files under the current folder.
You can ignore/remove files by specifying in the '-x' option.
This is a combination of the following commands:
`git a . -x <pathspec>`
`git commit -m <comment>`

Examples:
    1. Add all files and create a commit.
        git cia "This is the comment"
    2. Exclude *.config files, and create a commit.
        git -x *.config "This is the comment"
    3. Exclude the *.cs and *.config files, and create a commit.
        git -x *.config -x *.cs "This is the comment"
```
## git co
The usage is:
```

Check out the branch matching the string in <branch>.
If multiple branches include the <branch> text, all those branches will be listed and let user to choose.
This only works if '-b' is not present.
If '-b' is present, a new branch with name <branch> will be created.

Examples:
    Suppose we have 4 existing branches - master, develop, feature_1, feature_2
    1. Switch to an existing branch 'develop'
        git co develop
    2. Create a new branch 'feature_3'
        git co -b feature_3
    3. Create a new branch, and set the start point with <start_point>
        git co -b feature_3 32aa51b
    4. Switch to a branch with name like 'feature_*'
        gi co feature_
        
        Then it will list all indexed branches with 'feature_' in the name, and let the user to choose:
        
        Found 4 branches including "feature_":
        ====================
        0: feature_1
        1: feature_2
        ====================
        Please select branch by index:
        
        Then, the user can choose 0, click ENTER to switch to feature_1 branch.
```
## git llg
The usage is:
```

Show recent <number> logs, the default number is 5.
This is same as 'git log --oneline -n <number>'

Example:
    1. Show recent 5 commit messages.
        git llg
    2. Show recent 6 commit messages.
        git llg 6
```
## git m
The usage is:
```

Merge codes from branch <from> to current branch.
It will switch to branch <from>, pull the latest code, and then switch back to previous branch,
and merge the code from <from> into current branch. You need to make sure that there is no unstaged changes.

Examples:
    1. Merge latest code from master branch to current branch(develop)
        git m master
```
## git p
The usage is:
```

Pull the latest code from remote  with '--rebase' option.
It is same as 'git pull --rebase'
```
## git pr
The usage is:
```

Create pull request from current branch to <to_branch>.
Currently it only support to raise pull request to github and bitbucket.
The repository url is retrieved from the .git/config file.

Examples:
    1. Create PR against master branch
        git pr master
```
## git st
The usage is:
```

Show the working tree status, same as 'git status'
```
## git up
The usage is:
```

Create remote branch,
same as 'git push --set-upstream origin'
```
