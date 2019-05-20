from sys import argv

script, file_name = argv

print(f"We are removing the contents of the {file_name} !")
print("Is it Okay ? ")
print("If Yes, Press Ctrl+C to stop and If No, Press Return Key to continue", end = ' ')
input('> ')

fil = open(file_name, 'w')

print("Now, This file is going to be empty\n")
fil.truncate()

print("Now putting new 3 lines from input to the file\n")
line1 = input('> ')
line2 = input('> ')
line3 = input('> ')

print("Now these three lines are going to be written to the file")
fil.write(line1+"\n"+line2+"\n"+line3+"\n")

print("Closing the file !")
fil.close()