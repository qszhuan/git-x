from gity import Gity
import argparse
import sys
from utils import info

def init_parser():
    parser = argparse.ArgumentParser(description=info('Description: Add file contents to the index if specified in <--include>, remove file contents if specified in <--exclude>, then record changes to the repository'),
                                     epilog='')
    parser.add_argument("comment", type=str, help=info("The comment for the commit"))
    parser.add_argument("-i", "--include", nargs='*', type=str, help=info("Include the files that match the pattern(same as the <pathspec> for 'git add' command)"))
    parser.add_argument("-x", "--exclude", nargs='*', type=str, help=info("Exclude the files that match the pattern(same as the <pathspec> for 'git add' command)"))
    return parser

def main():
    parser = init_parser()
    args = parser.parse_args()
    gity = Gity()

    gity.ci(args.comment, args.include, args.exclude)

if __name__ == "__main__":
    main()

