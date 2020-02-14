Usages of all commands
==========================================

In the next we will show the detailed usage of each commands:

git x
-------------------------------------------

List out all the available commands:

::

  Usage: git-x [OPTIONS] COMMAND [ARGS]...
  
  Options:
    -h  Show this message and exit.
  
  Commands:
    a      Add file contents to the index
    amend  Amend files into repository
    b      Show current branch name
    ci     Commit all the indexed files
    cia    Add files into index and commit
    clb    Clean merged local branch.
    co     Checkout/Create branch
    llg    Show recent <number> logs
    m      Merge codes from branch <from> to current branch
    p      Pull latest code
    pr     Create pull request from current branch to <to_branch>
    st     Show the working tree status
    up     Create remote branch  
  
git a
-------------------------------------------

This is the description and example of this command:

::

  Usage: git-a [OPTIONS] <pathspec>
  
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
  
  Options:
    -x, --exclude <pathspec>  Exclude the files that match the pattern(same as
                              the <pathspec> for 'git add' command)
    -h                        Show this message and exit.
  
git amend
-------------------------------------------

This is the description and example of this command:

::

  Usage: git-amend [OPTIONS]
  
    Amend files into repository, this only amend the files that already in the index.
    
    Examples:
        1. Amend without editing
            git amend
        2. Amend, and edit the commit message, this will open the editing window,
            depends on what editor is configured in git.
            git amend -e
  
  Options:
    -e, --edit  Prompt edit window  [default: False]
    -h          Show this message and exit.
  
git b
-------------------------------------------

This is the description and example of this command:

::

  Usage: git-b [OPTIONS]
  
    Show current branch name.
    
    Example:
        git b
  
  Options:
    -h  Show this message and exit.
  
git ci
-------------------------------------------

This is the description and example of this command:

::

  Usage: git-ci [OPTIONS] <comment>
  
    Commit all the indexed files into repository, same as 'git commit -m <comment>'.
    
    Example:
        git ci "This is the comment."
  
  Options:
    -h  Show this message and exit.
  
git cia
-------------------------------------------

This is the description and example of this command:

::

  Usage: git-cia [OPTIONS] <comment>
  
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
  
  Options:
    -x, --exclude <pathspec>
    -h                        Show this message and exit.
  
git clb
-------------------------------------------

This is the description and example of this command:

::

  Usage: git-clb [OPTIONS]
  
    Clean merged local branch.
    It will always let user to confirm before remove.
    By default, it will ignore current branch and branches with name master, dev, develop, trunk.
    Because those branches are mostly used as trunk/release branches.
    
  
  Options:
    -h  Show this message and exit.
  
git co
-------------------------------------------

This is the description and example of this command:

::

  Usage: git-co [OPTIONS] <branch> <start_point>
  
    Check out the branch matching the string in <branch>.
    If multiple branches include the <branch> text, all those branches will be listed and let user to choose.
    This only works if '-b' is not present.
    If '-b' is present, a new branch with name <branch> will be created.
    
    Examples:
        Suppose we have 5 existing branches - master, develop, feature_1, feature_2, develop1
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
        5. Switch to a branch with -f option:
            gi co develop -f
            
            if there is a branch name exactly matching 'develop', it will check out that branch,
            no matter there are other branches with 'develop' in the name.
            If there is not exactly matches, then follow the same logic without -f option
            
            Found 1 branch exactly matching "develop":
            git co -b -f develop
  
  Options:
    -b  Indicate to create the branch if it doesn't exist, same to '-B' option
        in 'git checkout' command.  [default: False]
    -f  If set, checkout the branch directly without checking all brranches
        which name contains the <branch>
    -h  Show this message and exit.
  
git llg
-------------------------------------------

This is the description and example of this command:

::

  Usage: git-llg [OPTIONS] <number>
  
    Show recent <number> logs, the default number is 5.
    This is same as 'git log --oneline -n <number>'
    
    Example:
        1. Show recent 5 commit messages.
            git llg
        2. Show recent 6 commit messages.
            git llg 6
        3. Show with graph
            git llg -g
        4. Show with graph, author, and date
            git llg -gad
  
  Options:
    -g, --graph   Show in graph mode
    -a, --author  Show the author name of each commit
    -d, --date    show relative date of each commit
    -h            Show this message and exit.
  
git m
-------------------------------------------

This is the description and example of this command:

::

  Usage: git-m [OPTIONS] <from>
  
    Merge codes from branch <from> to current branch.
    It will switch to branch <from>, pull the latest code, and then switch back to previous branch,
    and merge the code from <from> into current branch. You need to make sure that there is no unstaged changes.
    
    Examples:
        1. Merge latest code from master branch to current branch(develop)
            git m master
  
  Options:
    -h  Show this message and exit.
  
git p
-------------------------------------------

This is the description and example of this command:

::

  Usage: git-p [OPTIONS]
  
    Pull the latest code from remote  with '--rebase' option.
    It is same as 'git pull --rebase'
  
  Options:
    -h  Show this message and exit.
  
git pr
-------------------------------------------

This is the description and example of this command:

::

  Usage: git-pr [OPTIONS] <to_branch>
  
    Create pull request from current branch to <to_branch>.
    Currently it only support to raise pull request to github and bitbucket.
    The repository url is retrieved from the .git/config file.
    
    Examples:
        1. Create PR against master branch
            git pr master
  
  Options:
    -h  Show this message and exit.
  
git st
-------------------------------------------

This is the description and example of this command:

::

  Usage: git-st [OPTIONS]
  
    Show the working tree status, same as 'git status'
  
  Options:
    -h  Show this message and exit.
  
git up
-------------------------------------------

This is the description and example of this command:

::

  Usage: git-up [OPTIONS]
  
    Create remote branch,
    same as 'git push --set-upstream origin'
  
  Options:
    -h  Show this message and exit.
  
