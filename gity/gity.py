# -*- coding: utf-8 -*-
from colorama import init

import sys
from pygments import highlight
from pygments.lexers import *
from pygments.formatters import *
import argparse
from shutil import copyfile
import datetime
from utils import *
import os

import subprocess

# use Colorama to make Termcolor work on Windows too
init(autoreset=True)

class Gity:
    def __init__(self):
        pass

    def st(self):
        call('git status')
    
    def p(self):
        cmd = 'git pull --rebase'
        print_info(f"Pull latest code ...[{cmd}]")
        call(cmd)
    
    def up(self):
        current_branch = self._current_branch()
        call(f"git push --set-upstream origin {current_branch}")
        
    def co(self, params):
        print_info(f'Checking out {params} ... ')
        call(f'git checkout {params}')
    
    def a(self, include, exclude):
        include_str = ' '.join(include) if include else None
        if(include_str):
            call(f'git add {include_str}')

        exclude_str = ' '.join(exclude) if exclude else None
        if(exclude_str):
            call(f'git reset {exclude_str}')
        
    def ci(self, comment, include, exclude):
        if(comment is None or comment == ''):
            raise Exception(error(f'Please add a valid comment.'))

        self.a(include, exclude)
            
        call(f'git commit -m "{comment}"')

    def cia(self, comment, exclude):
        if(comment is None or comment == ''):
            raise Exception(error(f'Please add a valid comment.'))
        self.a('.', exclude)
        call(f'git commit -am "{comment}"')
    
    def llg(self, n = 5):
        cmd = f'git log --oneline -n {n}'
        call(cmd)

    def pr(self, to_branch):
        remote_url = self._remote_url().rstrip('.git')
        current_branch = self._current_branch()
        if(to_branch == current_branch):
            print_error("Can't create pull request against the same branch")
            exit()
        else:
            print_info(f"Creating PR from {current_branch} to {to_branch}")
        
        old_start = "git@github.com:"
        if(remote_url.startswith(old_start)):
            remote_url = remote_url.replace(old_start, "https://github.com/")
        pr_url = f"{remote_url}/compare/{to_branch}...{current_branch}?expand=1"
        open_url(pr_url)

    def m(self, _from):
        if(_from is None):
            raise error("Please input source branch")

        _from = _from.strip()
        if(len(_from.split()) > 1):
            raise "Invalid parameter."

        currentBranch = self._current_branch()
        
        self.co(_from)
        self.p()
        print_info(f"Go back to {currentBranch}.")
        os.system(f'git checkout {currentBranch}')

        print_info(f'Merging the latest code from {_from} to {currentBranch} ...')
        os.system(f"git merge {_from}")

    def b(self):
        pass

    def _current_branch(self):
        branch = popen('git name-rev --name-only HEAD')
        print_info(f'Current branch: {branch}')
        return branch

    def _remote_url(self):
        cmd = "git config --get remote.origin.url"
        remote_url = popen(cmd)
        print_info(f'Remote origin url: {remote_url}')
        return remote_url

    


def init_parser():
    parser = argparse.ArgumentParser(description='git extensions',
                                     epilog=info('Try the green command listed above'))
    group = parser.add_mutually_exclusive_group()
    
    group.add_argument("-st", "--status", action="store_true", help=info("git st"))
    group.add_argument("-p", "--pull", action="store_true",  help=info("git p"))
    group.add_argument("-llg", "--logn", help=info("git llg [n]"))
    group.add_argument("-m", "--merge", help=info("git m [from]"))
    return parser

def main():
    parser = init_parser()
    args = parser.parse_args()
    gity = Gity()

    if args.status:
        gity.st()
    elif args.pull:
        gity.p()
    elif args.logn:
        gity.llg(args.logn)
    elif args.merge:
        gity.m(args.merge)
    else:
        parser.print_help()

    

if __name__ == '__main__':
    main()