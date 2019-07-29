# -*- coding: utf-8 -*-
from gity import Gity
import click
import argparse
from utils import *

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

@click.command(short_help=info("Similiar to [git add]"),
                help=info('Description : Add file contents to the index specified in pathspec, \
                remove file contents if specified in <--exclude>'))
@click.argument("pathspec", nargs=-1)
@click.option("-x",'--exclude', 
                help=info("Exclude the files that match the pattern(same as the <pathspec> for 'git add' command)"))
def a(pathspec, exclude):
    Gity().a(pathspec, exclude)

# parser = argparse.ArgumentParser(description=info('Description: Amend files to the repository'),
#                                      epilog='')
#     parser.add_argument("-i", "--include", nargs='*', type=str, help=info("Include the files that match the pattern(same as the <pathspec> for 'git add' command)"))
#     parser.add_argument("-x", "--exclude", nargs='*', type=str, help=info("Exclude the files that match the pattern(same as the <pathspec> for 'git add' command)"))
#     parser.add_argument("-e", "--edit", action='store_true', help=info("Exclude the files that match the pattern(same as the <pathspec> for 'git add' command)"))
   
@click.command(help=info("Amend files into repository"))
@click.option('-e', '--edit', is_flag=True)
@click.option('-i', '--include', 
        help=info("Include the files that match the pattern(same as the <pathspec> for 'git add' command)"))
@click.option('-x', '--exclude', nargs=100,
        help=info("Exclude the files that match the pattern(same as the <pathspec> for 'git add' command)"))
def amend(include, exclude, edit):
    Gity().amend(include, exclude, edit)


@click.command()
def b():
    pass
    
@click.command(help=info("Same as [git ci -m]"))
def ci():
    pass

@click.command(help=info("Add files into repository and commit"))
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
        short_help=info("Similiar to [git checkout]"))
@click.option('-b', metavar='create_if_not_existed', required=False, is_flag=True, help=info("Create new branch if it doesn't exist, same as the '-b' option in [git checkout]"))
@click.argument('branch', metavar='<branch>')
@click.argument('start_point', metavar='<start_point>', required=False)
def co(create_if_not_existed, branch, start_point):
    click.echo(branch, create_if_not_existed, start_point)
    #Gity().co()

@click.command("Show recent n logs(5 by default)")
def llg():
    pass

@click.command(help = info("Merge codes from another branch"))
def m():
    pass

@click.command(help = info('Same as [git pull --rebase]'))
def p():
    Gity().p()

@click.command(help=info('Create pull request'))
def pr():
    pass

@click.command(help = info("Same as [git status]"))
def st():
    Gity().st()

@click.command()
def up():
    pass


@click.group(context_settings=CONTEXT_SETTINGS)
def cli():
    pass

for each in [a, amend, b, ci, cia, co, llg, m, p, pr, st, up]:
    cli.add_command(each)

if __name__ == '__main__':
    cli()