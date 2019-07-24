import sys
import subprocess
from termcolor import colored
import os

is_windows = sys.platform == 'win32' or sys.platform == 'cygwin'
is_linux = 'linux' in sys.platform
is_mac = sys.platform == 'darwin'


class Platform(object):
    def is_windows(self):
        return sys.platform == 'win32' or sys.platform == 'cygwin'
    def is_linux(self):
        return 'linux' in sys.platform
    def is_mac(self):
        return sys.platform == 'darwin'

def call(command, exitOnError=True):
    print(colored(f'Execute [{command}]..', 'cyan'))
    if(subprocess.call(command)):
        print(colored(f"Error happened when running [{command}]", 'red'))
        if(exitOnError):
            exit()

def popen(command):
    return os.popen(command).read().strip()

def colored_decorator(color):
    def decorator(func):
        def wrapper(output):
            return colored(func(output), color)
        return wrapper
    return decorator

@colored_decorator('cyan')
def verbose(output):
    return output

@colored_decorator('green')
def info(output):
    return output

@colored_decorator('red')
def error(output):
    return output

def print_verbose(output):
    print(verbose(output))

def print_info(output):
    print(info(output))

def print_error(output):
    print(error(output))