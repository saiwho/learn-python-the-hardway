print('-'*80)
print('These commands are used to create a basic structure of project folder after creating virtual environment folder:')
print("""\tmkdir projects
        cd projects/
        mkdir projectname
        cd projectname
        mkdir bin NAME tests docs
        NAME folder -> for main scripts of the project or project's main module
        NAME can be renamed as root or main or project-name
        \nNow create some inital files:
        touch NAME/ __init__.py
        touch tests/ __init__.py
        \nCreate setup.py in the projectname folder and then copy this:
        try:
            from setuptools import setup
        except ImportError:
            from distutils.core import setup
            config = {
            'description': 'My Project',
            'author': 'My Name',
            'url': 'URL to get it at.',
            'download_url': 'Where to download it.',
            'author_email': 'My email.',
            'version': '0.1',
            'install_requires': ['nose'],
            'packages': ['NAME'],
            'scripts': [],
            'name': 'projectname'
            }
            setup(**config)
        
        \nCreate the test file for your project in tests folder prior to install nose package by pip for easy testing:
          Let be NAME_tests.py
            from nose.tools import *
            import NAME
            def setup():
                print("SETUP!")
            def teardown():
                print("TEAR DOWN!")
            def test_basic():
                print("I RAN!")
        \nFinal structure will be 
        projectname/
            NAME/
                __init__.py
            bin/
            docs/
            setup.py
            tests/
                NAME_tests.py
                __init__.py
        
        \nTo test our code we do,
        nosetests in the projectname directory

        \nThe bin directory contains the following:
        #!/usr/bin/env python

        from projectname import main

        if __name__ == '__main__':
        main()
        """)
