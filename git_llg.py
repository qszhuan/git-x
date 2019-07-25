from gity import Gity
import argparse
from utils import *

def check_positive(value):
    if(value is None):
        return None
    ivalue = int(value)
    if ivalue <= 0:
        raise argparse.ArgumentTypeError(error("%s is an invalid positive int value" % value))
    return ivalue

def init_parser():
    parser = argparse.ArgumentParser(description=info('Show the latest n commit in oneline mode'),
                                     epilog="")
    parser.add_argument("n", nargs='?', default=5, type=check_positive, help=info("The count of commits to show"))
    return parser


def main():
    parser = init_parser()
    args = parser.parse_args()
    gity = Gity()

    if args.n:
        gity.llg(args.n)
    else:
        parser.print_help()
    
if __name__ == "__main__":
    main()

