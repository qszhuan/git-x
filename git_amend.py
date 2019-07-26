from gity import Gity
import argparse
import sys
from utils import info

def init_parser():
    parser = argparse.ArgumentParser(description=info('Description: Amend files to the repository'),
                                     epilog='')
    parser.add_argument("-i", "--include", nargs='*', type=str, help=info("Include the files that match the pattern(same as the <pathspec> for 'git add' command)"))
    parser.add_argument("-x", "--exclude", nargs='*', type=str, help=info("Exclude the files that match the pattern(same as the <pathspec> for 'git add' command)"))
    parser.add_argument("-e", "--edit", action='store_true', help=info("Exclude the files that match the pattern(same as the <pathspec> for 'git add' command)"))
    return parser

def main():
    parser = init_parser()
    args = parser.parse_args()
    gity = Gity()

    gity.amend(args.include, args.exclude, args.edit)

if __name__ == "__main__":
    main()

