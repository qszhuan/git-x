from gity import Gity
import argparse

def init_parser():
    parser = argparse.ArgumentParser(description='git extensions',
                                     epilog='try replace gity with git')
    parser.add_argument("branch", type=str, help="The branch you want to merge from.")
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