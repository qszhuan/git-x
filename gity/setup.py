from setuptools import setup, find_packages

import os

git_scripts = [each for each in os.listdir() if each.startswith('git')]
git_extensions = [each.split('.')[0] for each in git_scripts] 
git_ex_entries = [f"{each.replace('_','-')}={each}:main" for each in git_extensions]

with open("../README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="Gity",
    version="0.1",
    packages=find_packages(),
    scripts=git_scripts,

    # Project uses reStructuredText, so ensure that the docutils get
    # installed or upgraded on the target machine
    install_requires=['docutils>=0.3'],

    package_data={
        # If any package contains *.txt or *.rst files, include them:
        '': ['*.txt', '*.rst'],
        # And include any *.msg files found in the 'hello' package, too:
        'hello': ['*.msg'],
    },

    # metadata to display on PyPI
   # Author details
    author='Qingshan Zhuan',
    author_email='zhuanqingshan@gmail.com',
    description="A set of handy git extensions",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords="git extension,git",
    url="https://github.com/qszhuan/gity",   # project home page, if any
    # project_urls={
    #     "Bug Tracker": "https://bugs.example.com/HelloWorld/",
    #     "Documentation": "https://docs.example.com/HelloWorld/",
    #     "Source Code": "https://code.example.com/HelloWorld/",
    # },

    # Choose your license
    license='MIT',

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

    py_modules= git_extensions,

    entry_points={
            'console_scripts': git_ex_entries,
        }

)