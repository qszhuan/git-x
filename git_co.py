from gity import Gity
import argparse
import sys
from utils import info

def init_parser():
    parser = argparse.ArgumentParser(description=info('This is an alias for "git checkout"'),
                                     epilog='')
    parser.add_argument("branch", type=str, help=info("Branch name to checkout"))
    parser.add_argument("-b", action='store_true', help=info("Create a new branch if not existed"))
    return parser

def main():
    parser = init_parser()
    args = parser.parse_args()
    gity = Gity()

    gity.co(args.branch, args.b)

if __name__ == "__main__":
    main()

