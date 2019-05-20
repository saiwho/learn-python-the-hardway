#importing commandline arguments libraries
from sys import argv

#splitting the command line arguments and storing each for further
script, filename = argv

#opening the filename and stroing as a string variable 
text = open(filename)
print(f"Here's your file {filename}")
#printing the string variable
print(text.read())

#For inputting the new file again we take input from the user
print("Type the file name again")
newfile = input('> ')

#Storing the newfile as string in the new string variable
newtext = open(newfile)
print("Printing the new file")
#Again printing the newtext contents i.e newfile
print(newtext.read())

