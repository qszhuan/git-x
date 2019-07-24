# -*- coding: utf-8 -*-
from colorama import Fore, Back, Style
from colorama import init
from termcolor import colored

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
        platform = Platform()
        self.platform = platform
        
    def st(self):
        call('git status')
    
    def p(self):
        cmd = 'git pull --rebase'
        print(colored(f"Pull latest code ...[{cmd}]", 'green'))
        call(cmd)

    def co(self, params):
        print(colored(f'Checking out {params} ... ', 'green'))
        call(f'git checkout {params}')
    
    def llg(self, n):
        cmd = f'git log --oneline -n {n}'
        call(cmd)

    def _current_branch(self):
        return popen('git symbolic-ref --short HEAD')

    def m(self, _from):
        if(_from is None):
            raise "Please input source branch"

        _from = _from.strip()
        if(len(_from.split()) > 1):
            raise "Invalid parameter."

        currentBranch = self._current_branch()
        print(colored(f"Current branch: {currentBranch}", 'cyan'))
        
        self.co(_from)
        self.p()
        print(colored(f"Go back to {currentBranch}.", 'green'))
        os.system(f'git checkout {currentBranch}')

        print(colored(f'Merging the latest code from {_from} to {currentBranch} ...', 'green'))
        os.system(f"git merge {_from}")

    def b(self):
        pass


def init_parser():
    parser = argparse.ArgumentParser(description='git extensions',
                                     epilog='try replace gity with git')
    group = parser.add_mutually_exclusive_group()
    
    group.add_argument("-st", "--status", action="store_true", help="git status")
    group.add_argument("-p", "--pull", action="store_true",  help="git pull --rebase")
    group.add_argument("-llg", "--logn", help="git log --oneline -n *")
    group.add_argument("-m", "--merge", help="git merge [from]")
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