# This is very good practice of making virtual environments rather than installing all the modules in usr/lib 
# This is how we do it

print('In this exercise we learn about setting up virtual environment for projects ')
print("""Virtual environments are important as different projects requires different 
        python versions and different modules and help organise projects
        and it's packages easier""")

print('\n')
print('*'*30 + ' Follow these steps '+ '*'*30)
print('\n')
print('-'*75)
print('These are the important build libraries for python virtual environment:')
print('sudo apt-get install build-essential libssl-dev libffi-dev python-dev')
print('\n')
print('-'*75)
print('Installing virtual environment package:')
print('sudo apt install python3-venv')
print('\n')
print('-'*75)
print('make a directory with the name related to project and if needed give version number like 3.5 or 3.67 etc,..')
print('python3 -m venv foldername -> copies the files needed for virtual environment to foldername')
print('\n')
print('-'*75)
print('To activate the environment:')
print('source foldername/bin/activate')
print('\n')
print('-'*75)
print('Install any packages needed for the project here')
print('pip3 install packagename')
print('\n')
print('-'*75)
print('To deactivate the virtual environment:')
print('deactivate')