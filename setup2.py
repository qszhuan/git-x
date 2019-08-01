import sys
from cx_Freeze import setup, Executable
import cli

executables = [Executable('git_{}.py'.format(each.name), targetName= 'git-{}.exe'.format(each.name)) for each in cli.all_commands()]
executables.append(Executable("cli.py",targetName='gity.exe'))

setup(  
    name = "gity",
    version = cli.__version__,
    description = cli.__doc__,
    author= cli.__author__,
    options = {
        "bdist_msi": {
            'add_to_path': True,
            'upgrade_code': True
        },
    },
    executables = executables
)