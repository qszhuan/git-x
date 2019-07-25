from gity import Gity
import argparse
import sys
from utils import *

def init_parser():
    parser = argparse.ArgumentParser(description=info(f'Create branch on remote if not existed and push codes'),
                                     epilog='')
    return parser


def main():
    args = sys.argv
    
    parser = init_parser()
    if('-h' in args or '--help' in args):
        parser.print_help()
        exit()
    
    gity = Gity()
    gity.up()

if __name__ == "__main__":
    main()

