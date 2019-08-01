import sys
from cx_Freeze import setup, Executable
import cli

executables = [Executable('git_{}.py'.format(each.name), targetName= 'git-{}.exe'.format(each.name)) for each in cli.all_commands()]
executables.append(Executable("cli.py",targetName='gity.exe'))



setup(  name = "gity",
        version = "1.0.0",
        description = "A set of handy git extensions",
        options = {
            "bdist_msi": {
                'add_to_path': True,
                'upgrade_code': True
            },
        },
        executables = executables)