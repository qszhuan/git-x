from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand

import os
import sys
import cli

command_names = [each.name for each in cli.all_commands()]
modules = ['cli', 'gity', 'utils']
git_scripts = ['cli.py','gity.py']

git_ex_entries = ["git-{}=cli:{}".format(each, each) for each in command_names]
git_ex_entries.append("gity=cli:main")

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
            '--doctest-modules', '--verbose', '--cov=.',
            './tests'
        ]
        self.test_suite = True

    def run_tests(self):
        import pytest
        sys.exit(pytest.main(self.test_args))


tests_require = [
    # Pytest needs to come last.
    # https://bitbucket.org/pypa/setuptools/issue/196/
    'pytest',
    'pytest-cov',
    'mock',
]

## depencencies
install_requires = [
    'click',
]

# Conditional dependencie

setup(
    name="gity",
    version=cli.__version__,
    packages=find_packages(),
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
    author=cli.__author__,
    author_email='zhuanqingshan@gmail.com',
    description=cli.__doc__,
    long_description=long_description,
    keywords="git extension,git, gity",
    url="https://github.com/qszhuan/gity",   # project home page, if any
    project_urls={
        "Bug Tracker": "https://github.com/qszhuan/gity/issues",
        "Documentation": "https://github.com/qszhuan/gity/wiki",
        "Source Code": "https://github.com/qszhuan/gity",
    },

    # Choose your license
    license=cli.__license__,

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