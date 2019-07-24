from gity import Gity
import argparse
import sys
from utils import info

def init_parser():
    parser = argparse.ArgumentParser(description=info(f'This is an alias for "git checkout"'),
                                     epilog='')
    return parser

def main():
    args = sys.argv
    gity = Gity()
    
    parser = init_parser()
    if('-h' in args or '--help' in args):
        parser.print_help()
        exit()
    
    arg_str = ' '.join(map(str, args[1:])) 
    gity.co(arg_str)

if __name__ == "__main__":
    main()

