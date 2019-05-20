#importing sys package or module for argv 
from sys import argv

script, file_name = argv

# fn for printing all the lines of the file
def print_all(filein):
    print(filein.read())

# fn to move the current location of the pointer to the starting position
def rewind(filein):
    filein.seek(0)

#fn to print one line at a time
def print_one_at_a_time(filein):
    print(filein.readline())

print(f"This is the name of the file {file_name} you have given as one of argument")

# Opening file in read mode
fileread = open(file_name)

# Printing all the contents of the file
print_all(fileread)

# Moving the cursor to the home position
rewind(fileread)

#Printing one line at a time
line_count = 0
line_count += 1
print(f"First line : {line_count}")
print_one_at_a_time(fileread)
line_count += 1
print(f"Second line : {line_count}")
print_one_at_a_time(fileread)
line_count += 1
print(f"Third line : {line_count}")
print_one_at_a_time(fileread)

print("Finally learnt using file operations using own functions")