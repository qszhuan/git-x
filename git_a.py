from gity import Gity
import argparse
import sys
from utils import info

def init_parser():
    parser = argparse.ArgumentParser(description=info(f'Description: Add file contents to the index specified in pathspec, remove file contents if specified in <--exclude>'),
                                     epilog='')
    parser.add_argument("pathspec", nargs = '*', type=str, help=info("Include the files that match the pattern(same as the <pathspec> for 'git add' command)"))
    parser.add_argument("-x", "--exclude", nargs='*', type=str, help=info("Exclude the files that match the pattern(same as the <pathspec> for 'git add' command)"))
    return parser

def main():
    parser = init_parser()
    args = parser.parse_args()
    gity = Gity()

    gity.a(args.pathspec, args.exclude)

if __name__ == "__main__":
    main()

