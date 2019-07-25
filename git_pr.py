from gity import Gity
import argparse
from utils import *


def init_parser():
    parser = argparse.ArgumentParser(description=info('Generate a pull request from current branch to another branch, and open it by the default browser on your machine.'),
                                     epilog=warning('Currently it supports to create pull request on github only.'))
    parser.add_argument("target_branch", type=str, help=info("The target branch for pull request"))
    return parser

def main():
    parser = init_parser()
    args = parser.parse_args()
    gity = Gity()

    if args.target_branch:
        gity.pr(args.target_branch)
    else:
        parser.print_help()
if __name__ == "__main__":
    main()

