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

.. |version| image:: https://img.shields.io/pypi/v/git-x?color=green&style=plastic
    :alt: PyPI

.. |pypi_format| image:: https://img.shields.io/pypi/format/git-x
    :alt: PyPI - Format


==========================================
git-x - a set of handy git extensions.
==========================================

Installation
==========================================

.. code-block:: text

  pip install git-x --upgrade  

How to Use
==========================================

Show help  message
-----------------------------------------

Run 

.. code-block:: sh

  git-x 

, or ignore the ``-`` in ``git-x``:


.. code-block:: sh

  git x


It will output the help message, which showing all the available commands:

.. code-block:: sh

  $ git x
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

  git-x st -h

It will output the help doc of ``st`` command:

.. code-block::

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

Please read the Usage_ to see all the available commands.

.. _Usage: usage.rst

**Notice**:

 You need to install git cli tool first, as all the commands will call the native git commands eventually.


Finally, happy ``git``-ing with ``git-x``.


