.. start-badges

.. list-table::
    :stub-columns: 1

    * - License
      - |license|
    * - CI
      - |travis|
    * - Packages
      - |version| |pypi_format| |supported-versions|

.. |travis| image:: https://travis-ci.org/qszhuan/git-x.svg?branch=master
    :target: https://travis-ci.org/qszhuan/git-x

.. |license| image:: https://img.shields.io/github/license/qszhuan/git-x?style=plastic
    :alt: GitHub license
    :target: https://github.com/qszhuan/git-x/blob/master/LICENSE

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/git-x
    :alt: PyPI - Python Version

.. |version| image:: https://img.shields.io/pypi/v/git-x?style=plastic
    :alt: PyPI

.. |pypi_format| image:: https://img.shields.io/pypi/format/git-x
    :alt: PyPI - Format


==========================================
git-x - a set of handy git extensions.
==========================================

Installation
==========================================

.. code-block:: text

  pip install git-x

How to Run
==========================================

Show help  message
-----------------------------------------

Run 

.. code-block:: sh

  git-x 

, or ignore the ``-`` in ``git-x``:


.. code-block:: sh

  git x


It will output the help message:

.. code-block:: sh

  $ git x
  Usage: git-x [OPTIONS] COMMAND [ARGS]...

  Options:
    -h  Show this message and exit.

  Commands:
    a      Add files to the index
    amend  Amend files into repository
    b      Show current branch name
    ci     Commit all the indexed files
    cia    Add files into index and commit
    co     Check out branch <branch>, create if '-b' is True and the branch
          doesn't exist.
    llg    Show recent <number> logs(5 by default)
    m      Merge codes from branch <from>
    p      Same as [git pull --rebase]
    pr     Create pull request from current branch to <to_branch>
    st     Show file status
    up     Create remote branch


*Note: If you have an exe like* ``git-x.exe`` *in windows, or* ``git-x.sh`` *in linux or mac, you can run the command with* ``git x`` *directly. This is handled by git.*

Run commands
------------------------------


``git-x`` includes a list of commands, let's take ``st`` as an example:

There are several ways to run the command:

1. Run with ``git-x``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Run

.. code-block:: sh  

 git x st -h 


Or,

 .. code-block:: sh

  git-x sh -h

It will output the help doc of ``sh`` command:

.. code-block:: sh

  $ git x st -h
  Usage: git-x st [OPTIONS]

    Show file status, same as 'git status'

  Options:
    -h  Show this message and exit.

2. Run with ``git-`` or ``git``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You may see that in the Usage line, it shows ``git-st``, which means that you can run the commands listed above with ``git-``:

.. code-block:: sh

  git-st -h

Or, even run with ``git``:

.. code-block:: sh

  git st -h

They both output the help doc of ``st`` command:

.. code-block:: sh

  $ git-st -h
  Usage: git-st [OPTIONS]

    Show file status, same as 'git status'

  Options:
    -h  Show this message and exit.


Usages of all commands
==========================================

git st
------

List out all the available commands:

::

   a        Add file contents to the index
   amend    Amend files into repository
   b        Show current branch name
   ci       Commit all the indexed files
   cia      Add files into index and commit
   co       Checkout/Create branch
   llg      Show recent <number> logs
   m        Merge codes from branch <from> to current branch
   p        Pull latest code
   pr       Create pull request from current branch to <to_branch>
   st       Show the working tree status
   up       Create remote branch

git a
-----

The usage is:

::


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

git amend
---------

The usage is:

::


   Amend files into repository, this only amend the files that already in the index.

   Examples:
       1. Amend without editing
           git amend
       2. Amend, and edit the commit message, this will open the editing window,
           depends on what editor is configured in git.
           git amend -e

git b
-----

The usage is:

::


   Show current branch name.

   Example:
       git b

git ci
------

The usage is:

::


   Commit all the indexed files into repository, same as 'git commit -m <comment>'.

   Example:
       git ci "This is the comment."

git cia
-------

The usage is:

::


   Add content files into index, and then create a new commit.
   By default it will add all the files under the current folder.
   You can ignore/remove files by specifying in the '-x' option.
   This is a combination of the following commands:
   'git a . -x <pathspec>'
   'git commit -m <comment>'

   Examples:
       1. Add all files and create a commit.
           git cia "This is the comment"
       2. Exclude *.config files, and create a commit.
           git -x *.config "This is the comment"
       3. Exclude the *.cs and *.config files, and create a commit.
           git -x *.config -x *.cs "This is the comment"

git co
------

The usage is:

::


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

**Notice**: 

 You need to install git cli tool first, as all the commands will call the native git commands eventually.


Finally, happy ``git``-ing with ``git-x``.


