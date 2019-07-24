from gity import Gity
import argparse
import sys
from utils import *

def init_parser():
    parser = argparse.ArgumentParser(description=info(f'This is an alias for "git commit -m"'),
                                     epilog='')
    parser.add_argument("comment", nargs='?', type=str, help=info("The comment for the commit"))
    parser.add_argument("-i", "--include", nargs='*', type=str, help=info("Include the files that match the pattern(same as the <pathspec> for 'git add' command)"))
    parser.add_argument("-x", "--exclude", nargs='*', type=str, help=info("Exclude the files that match the pattern(same as the <pathspec> for 'git add' command)"))
    return parser

def main():
    parser = init_parser()
    args = parser.parse_args()
    gity = Gity()

    if args.comment:
        gity.ci(args.comment, args.include, args.exclude)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()

