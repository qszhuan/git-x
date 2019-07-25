from gity import Gity
import argparse
from utils import *

def init_parser():
    parser = argparse.ArgumentParser(description=info('Merge the latest n commits from another branch into current branch.'),
                                     epilog='Merge the latest code from another branch.')
    parser.add_argument("branch", type=str, help=info("The branch you want to merge from"))
    return parser

def main():
    parser = init_parser()
    args = parser.parse_args()
    gity = Gity()

    if args.branch:
        gity.m(args.branch)
    else:
        parser.print_help()
if __name__ == "__main__":
    main()