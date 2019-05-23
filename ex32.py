#List of integers
the_count = [1, 2, 3, 4, 5]
#List of strings
fruits = ['oranges', 'mangoes', 'bananas', 'apples' ]
#List of integers and strings
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

#Printing each element in list the_count
for no in the_count:
    print(f"The count is {no}")

#Printing each element in list fruits
for fruit in fruits:
    print(f"A fruit of type {fruit}")

#Printing each element in list change
for i in change:
    print(f'I got change {i}')

#Defining the empty list
elements = []

#Building the list using range function and loop
for i in range(0,6):
    print(f"Adding {i} to the list")
    elements.append(i)

print("\n")
#Printing the newly created list
print("New elements are :")
for i in elements:
    print(i)
