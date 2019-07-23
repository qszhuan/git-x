from setuptools import setup, find_packages

setup(
    name="Gity",
    version="0.1",
    packages=find_packages(),
    scripts=['gity.py', 
                'git-pr.py', 
                'git_m.py', 
                'git_st.py', 
                'git_p.py',
                'git_co.py'],

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
        'Intended Audience :: System Administrators',
        'Topic :: Utilities',
        'Topic :: Software Development',
        'Topic :: Terminals',
        'Topic :: Version Control',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

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

    
    classifiers=[
        'License :: OSI Approved :: Python Software Foundation License'
    ],
    py_modules=["gity", "git_st", 'git_p', "utils"],

    entry_points={
            'console_scripts': [
                'git-p=git_p:main',
                'git-st=git_st:main',
                'gity=gity:main'
            ],
        }

    # could also include long_description, download_url, etc.
)