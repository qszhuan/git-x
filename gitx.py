# -*- coding: utf-8 -*-

import sys
import argparse
import datetime
from utils import *
import os

class Gitx:
    def __init__(self):
        pass

    def st(self):
        call('git status')
    
    def p(self):
        cmd = 'git pull --rebase'
        print_info("Pull latest code ...[{}]".format(cmd))
        call(cmd)
    
    def up(self):
        current_branch = self._current_branch()
        call("git push --set-upstream origin {}".format(current_branch))
        
    def co(self, branch, start_point=None, create_if_not_existed=False):
        print_info('Checking out {} ... '.format(branch))
        create_option = "-b" if create_if_not_existed else ''
        
        call('git checkout {} {} {}'.format(create_option, branch, start_point if start_point else ''))
    
    def a(self, include, exclude):
        include_str = ' '.join(include) if isinstance (include, list) else include
        if(include_str):
            call('git add {}'.format(include_str))

        exclude_str = ' '.join(exclude) if isinstance (exclude, list) else exclude
        if(exclude_str):
            call('git reset {}'.format(exclude_str))
        
    def ci(self, comment, include, exclude):
        if(comment is None or comment == ''):
            raise Exception(error('Please add a valid comment.'))

        self.a(include, exclude)
            
        call('git commit -m "{}"'.format(comment))

    def amend(self, include, exclude, edit):
        self.a(include, exclude)
        cmd = 'git commit --amend --no-edit' if not edit else 'git commit --amend'
        call(cmd)

    def cia(self, comment, exclude):
        if(comment is None or comment == ''):
            raise Exception(error('Please add a valid comment.'))
        self.a('.', exclude)
        call('git commit -am "{}"'.format(comment))
    
    def llg(self, n = 5):
        cmd = 'git log --oneline -n {}'.format(n)
        call(cmd)

    def pr(self, to_branch):
        remote_url = self._remote_url().rstrip('.git')
        current_branch = self._current_branch()
        if(to_branch == current_branch):
            print_error("Can't create pull request against the same branch")
            exit()
        else:
            print_info("Creating PR from {} to {}".format(current_branch, to_branch))
        
        old_start = "git@github.com:"
        if(remote_url.startswith(old_start)):
            remote_url = remote_url.replace(old_start, "https://github.com/")
        pr_url = "{}/compare/{}...{}?expand=1".format(remote_url, to_branch, current_branch)
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
        print_info("Go back to {}.".format(currentBranch))
        os.system('git checkout {}'.format(currentBranch))

        print_info('Merging the latest code from {} to {} ...'.format(_from, currentBranch))
        os.system("git merge {}".format(_from))

    def b(self):
        self._current_branch()

    def _current_branch(self):
        branch = popen('git name-rev --name-only HEAD')
        print_info('Current branch: {}'.format(branch))
        return branch

    def _remote_url(self):
        cmd = "git config --get remote.origin.url"
        remote_url = popen(cmd)
        print_info('Remote origin url: {}'.format(remote_url))
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
    gitx = Gitx()

    if args.status:
        gitx.st()
    elif args.pull:
        gitx.p()
    elif args.logn:
        gitx.llg(args.logn)
    elif args.merge:
        gitx.m(args.merge)
    else:
        parser.print_help()

    

if __name__ == '__main__':
    main()