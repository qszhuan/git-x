.. image:: https://travis-ci.org/qszhuan/git-x.svg?branch=master
    :target: https://travis-ci.org/qszhuan/git-x

==========================================
git-x - a set of handy git extensions.
==========================================

Installation
==========================================

.. code-block:: text

  pip install git-x

Execution
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


*Note: If you have an exe like ``git-x.exe`` in windows, or ``git-x.sh`` in linux or mac, you can run the command with ``git x`` directly. This is handled by git.*


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

It will output the help docof ``sh`` command:

.. code-block:: sh

  $ git x st -h
  Usage: git-x st [OPTIONS]

    Show file status, same as 'git status'

  Options:
    -h  Show this message and exit.

2. Run with ``git-``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You may see that in the Usage line, it shows ``git-st``, which means that you can run the commands listed above with ``git-``:

.. code-block:: sh

  git-st -h

It will output the same result:

.. code-block:: sh

  $ git-st -h
  Usage: git-st [OPTIONS]

    Show file status, same as 'git status'

  Options:
    -h  Show this message and exit.


3. Run with ``git``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

As mentioned above, we can also run the command with ``git`` directly.

.. code-block:: sh

  git st -h 


It will do the same as ``git x sh -h`` or ``git-x sh -h``.

**Notice**: 

1. You may know that you can add git alias in the git config file. If you have the same alias added, the alias will not be invoked:

  .. code-block:: ini

    [alias]
    st=status

2. You need to install git cli tool first, as all the commands will call the native git commands eventually.


Finally, happy ``git``-ing with ``git-x``.


