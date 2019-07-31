from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand

import os
import sys
import cli

# entry_points and scripts
# git_scripts = [each for each in os.listdir('.') if each.endswith('.py') and not each.startswith('setup')]
# git_extensions = [each.split('.')[0] for each in git_scripts] 
command_names = [each.name for each in cli.all_commands()]
modules = ['cli', 'gity']
git_scripts = ['cli.py','gity.py']

git_ex_entries = ["git-{}=cli:{}".format(each, each) for each in command_names]
git_ex_entries.append("gity=cli:main")

print(git_ex_entries)
# README
with open("README.md", "r") as fh:
    long_description = fh.read()

#Tests
class PyTest(TestCommand):
    # `$ python setup.py test' simply installs minimal requirements
    # and runs the tests with no fancy stuff like parallel execution.
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = [
            '--doctest-modules', '--verbose',
            '.', './tests'
        ]
        self.test_suite = True

    def run_tests(self):
        import pytest
        sys.exit(pytest.main(self.test_args))


tests_require = [
    # Pytest needs to come last.
    # https://bitbucket.org/pypa/setuptools/issue/196/
    'pytest',
    'mock',
]

## depencencies
install_requires = [
    'colorama',
    'termcolor'
]


# Conditional dependencies:

# sdist
if 'bdist_wheel' not in sys.argv:
    try:
        # noinspection PyUnresolvedReferences
        import argparse
    except ImportError:
        install_requires.append('argparse>=1.2.1')

    if 'win32' in str(sys.platform).lower():
        # Terminal colors for Windows
        install_requires.append('colorama>=0.2.4')

# bdist_wheel
extras_require = {
    # http://wheel.readthedocs.io/en/latest/#defining-conditional-dependencies
    'python_version == "3.0" or python_version == "3.1"': ['argparse>=1.2.1'],
    ':sys_platform == "win32"': ['colorama>=0.2.4'],
}

setup(
    name="Gity",
    version='1.0.0.dev',
    packages=find_packages(),
    scripts=git_scripts,
    extras_require=extras_require,
    install_requires=install_requires,
    tests_require=tests_require,
    cmdclass={'test': PyTest},

    # Project uses reStructuredText, so ensure that the docutils get
    # installed or upgraded on the target machine

    package_data={
        # If any package contains *.txt or *.rst files, include them:
        '': ['*.txt', '*.rst', '*.md', 'LICENSE'],
    },

    # metadata to display on PyPI
   # Author details
    author="Qingshan Zhuan",
    author_email='zhuanqingshan@gmail.com',
    description="A set of handy git extensions",
    long_description=long_description,
    keywords="git extension,git",
    url="https://github.com/qszhuan/gity",   # project home page, if any
    project_urls={
        "Bug Tracker": "https://github.com/qszhuan/gity/issues",
        "Documentation": "https://github.com/qszhuan/gity/wiki",
        "Source Code": "https://github.com/qszhuan/gity",
    },

    # Choose your license
    license="MIT",

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Topic :: Utilities',
        'Topic :: Software Development',
        'Topic :: Terminals',
        'Topic :: Version Control',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        "Operating System :: OS Independent",

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    py_modules=modules,
    entry_points={
            'console_scripts': git_ex_entries,
        }

)