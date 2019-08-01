[![Build Status](https://travis-ci.org/qszhuan/git-x.svg?branch=master)](https://travis-ci.org/qszhuan/git-x)

# git-x

git-x - a set of handy git extensions.


## Installation

```
pip install git-x
```

## Usage

Run 

```sh
git-x 
```
, or
```sh
git x
```
It will output:

```
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
```

It includes a list of command, take `st` as an example:

Run
```sh
git x st -h 
```
It will output the help doc:

```sh
$ git x st -h
Usage: git-x st [OPTIONS]

  Show file status, same as 'git status'

Options:
  -h  Show this message and exit.
```

Actually, for the commands, the `x` can be ignored, like:

```sh
git st -h 
```

It will do the same as `git x sh -h` or `git-x sh -h`.

You can also add `-` between  `git` and `st`, like:

```
git-st -h
```

Please notice: You need to install git cli tool first, as all the commands will call the native `git` commands eventually.




