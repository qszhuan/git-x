# -*- coding: utf-8 -*-
from gity import Gity
import click
import argparse
from utils import *

CONTEXT_SETTINGS = dict(help_option_names=['-h'])

@click.command(short_help="Add files to the index",
                help=info('Add file contents to the index specified in pathspec, \
                remove file contents if specified in <--exclude>'))
@click.argument("pathspec", nargs=-1, metavar='<pathspec>')
@click.option("-x", '--exclude', 
                metavar='<pathspec>', 
                multiple=True,
                help=info("Exclude the files that match the pattern(same as the <pathspec> for 'git add' command)"))
def a(pathspec, exclude):
    Gity().a(list(pathspec), list(exclude))

@click.command(help="Amend files into repository, this only amend the files that already in the index.",
                short_help="Amend files into repository")
@click.option('-e', '--edit', is_flag=True, show_default=True, help="Prompt edit window")
def amend(edit):
    Gity().amend(None, None, edit)


@click.command(help='Show current branch name')
def b():
    Gity().b()
    
@click.command(short_help="Commit all the indexed files")
@click.argument('comment', metavar='<comment>')
def ci(comment):
    """Commit all the indexed files into reposity, same as 'git commit -m <comment>'.
    """
    Gity().ci(comment, None, None)

@click.command(short_help="Add files into index and commit")
@click.argument('comment', metavar='<comment>')
@click.option('-x', '--exclude', metavar='<pathspec>', required=False, multiple=True)
def cia(comment, exclude):
    """Add files into index, and then commit to repository. \n
    This is a combination of the following commands: \n
    `git a . -x <pathspec>` \n
    `git commit -m <comment>`
    """
    Gity().cia(comment, list(exclude))

# parser.add_argument("branch", type=str, help=info("Branch name to checkout"))
#     parser.add_argument("-b", action='store_true', help=info("Create a new branch if not existed"))

co_help = """Check out branch <branch>, create if '-b' is True and the branch doesn't exist. \n
This is similiar to 'git checkout', but doesn't support other parameters.
"""
@click.command( 
        help=co_help, 
        short_help="Check out branch <branch>, create if '-b' is True and the branch doesn't exist.")
@click.option('-b', metavar='create_if_not_existed', required=False, 
                is_flag=True, 
                show_default=True,
                help="Indicate to create the branch if it doesn't exist, same to '-B' option in 'git checkout' command.")
@click.argument('branch', metavar='<branch>')
@click.argument('start_point', metavar='<start_point>', required=False)
def co(start_point, b, branch):
    print(branch, b, start_point)
    Gity().co(branch, start_point, b)

@click.command(short_help="Show recent <number> logs(5 by default)",)
@click.argument('n', metavar='<number>', default=5)
def llg(n):
    """Show recent <number> logs(5 by default), same to 'git log --oneline -n <number>'
    """
    Gity().llg()

@click.command(help="Merge codes from branch <from>")
@click.argument('from_', metavar='<from>')
def m(from_):
    Gity().m(from_)

@click.command(help='Same as [git pull --rebase]')
def p():
    Gity().p()

@click.command(short_help='Create pull request from current branch to <to_branch>')
@click.argument('to_branch', metavar='<to_branch>', nargs=1)
def pr(to_branch):
    """Create pull request from current branch to <to_branch>.
    Currently it only support to raise pull request to github.
    The github repo url is retrieved from the .git/config file.
    """
    Gity().pr(to_branch)

@click.command(short_help="Show file status")
def st():
    """Show file status, same as 'git status'"""
    Gity().st()

@click.command(short_help="Create remote branch")
def up():
    """Create remote branch, 
    same as 'git push --set-upstream origin'
    """
    Gity().up()


@click.group(context_settings=CONTEXT_SETTINGS)
def main():
    pass

def all_commands():
    return  [a, amend, b, ci, cia, co, llg, m, p, pr, st, up]
    
for each in all_commands():
    each.context_settings=CONTEXT_SETTINGS
    main.add_command(each)

if __name__ == '__main__':
    main()