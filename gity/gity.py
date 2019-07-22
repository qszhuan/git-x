# -*- coding: utf-8 -*-

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


class Gity:
    def __init__(self):
        platform = Platform()
        self.platform = platform
        
    def st(self):
        os.system('git status')
    
    def p(self):
        os.system('git pull --rebase')

    def co(self, params):
        os.system(f'git checkout {params}')
    
    def llg(self, n):
        os.system(f'git log --oneline -n {n}')

    def m(self, _from):
        if(_from is None):
            raise "Please choose source branch"
        
        currentBranch = os.popen('git symbolic-ref --short HEAD').read().strip()
        print(f'Merging the code from {_from} to {currentBranch}')
        print(f"Current branch: {currentBranch}")
        os.system(f'git checkout {_from}')
        print(f"Pull branch {_from} latest code...")
        self.p()
        print(f"Go back to {currentBranch}.")
        os.system(f'git checkout {currentBranch}')

        print(f"Merging {_from} into {currentBranch} ...")
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