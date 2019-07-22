from gity import Gity
import argparse
import sys

def init_parser():
    parser = argparse.ArgumentParser(description='This is an alias for "git checkout"',
                                     epilog='')
    return parser

def main():
    args = sys.argv
    gity = Gity()
    print(f'xx {args}')
    
    arg_str = ' '.join(map(str, args[1:])) 
    gity.co(arg_str)

if __name__ == "__main__":
    main()

