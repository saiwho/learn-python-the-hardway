numbers = []
i = 0

print("Here defines the condition for the while loop for exit")
while i < 6:
    print(f"Appending number: {i} to the list")
    numbers.append(i)
    i += 1
print(f"Value of i at the end of the while loop is {i}")

print("The numbers of new list are: ")
for i in range(len(numbers)):
    print(i)

print("list of numbers list is", numbers)