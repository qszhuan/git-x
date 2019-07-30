# -*- coding: utf-8 -*-
from gity import Gity
import click
import argparse
from utils import *

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

@click.command(short_help="Add files to the index",
                help=info('Description : Add file contents to the index specified in pathspec, \
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
    """Commit all the indexed files into reposity, same as 'git commit -m'.
    """
    Gity().ci(comment, None, None)

@click.command(help="Add files into repository and commit")
def cia():
    pass

# parser.add_argument("branch", type=str, help=info("Branch name to checkout"))
#     parser.add_argument("-b", action='store_true', help=info("Create a new branch if not existed"))

co_help = info("""Similiar to [git checkout] \n
This is not an alias of [git checkout]. \n
In order to keep it simple, it only accepts two arguments: BRANCH,  and -b

""") 
@click.command( 
        help=co_help, 
        short_help="Create new branch if it doesn't exist, same as the '-b' option in [git checkout]")
@click.option('-b', metavar='create_if_not_existed', required=False, 
                is_flag=True, 
                show_default=True,
                help=info("Create new branch if it doesn't exist, same as the '-b' option in [git checkout]"))
@click.argument('branch', metavar='<branch>')
@click.argument('start_point', metavar='<start_point>', required=False)
def co(start_point, b, branch):
    print(branch, b, start_point)
    Gity().co(branch, start_point, b)

@click.command(help="Show recent n logs(5 by default)")
def llg():
    pass

@click.command(help="Merge codes from branch <from>")
@click.argument('from_', metavar='<from>')
def m(from_):
    Gity().m(from_)

@click.command(help='Same as [git pull --rebase]')
def p():
    Gity().p()

@click.command(help='Create pull request')
def pr():
    pass

@click.command(help="Same as [git status]")
def st():
    Gity().st()

@click.command(help="create remote branch")
def up():
    pass


@click.group(context_settings=CONTEXT_SETTINGS)
def cli():
    pass

for each in [a, amend, b, ci, cia, co, llg, m, p, pr, st, up]:
    cli.add_command(each)

if __name__ == '__main__':
    cli()