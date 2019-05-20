from sys import argv
from os.path import exists

script, fromfile, tofile = argv

print(f"We are now going to copy contents from {fromfile} to {tofile}")

# Printing the no of bytes of the fromfile
print(f"Printing the no of bytes of {fromfile}\n", len(fromfile))

# Opening the fromfile in read mode and reading, storing in datain
# We can combine these two statements into datain = open(fromfile, 'r').read()
inn = open(fromfile,'r')
datain = inn.read()

# Checking if tofile exists or not ?
print(f"Does {tofile} exists ?")
print(exists(tofile))
print("If not creating one")

#Opening tofile and writing the data
print(f"Opening {tofile} and writing the data")
outt = open(tofile, 'w')
outt.write(datain)
print(f"Now we have successfully written the data to {tofile}")

print("All work is done")
outt.close()
inn..close()