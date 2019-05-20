# Basic string formatting, escape characters, newline and tab
print("Let's practice everytime to get accustomed with Python")
print("These is also known as \'escape\' characters and This is \"crazy\"")
print("\nThis is newline and \t This is tab")

#String of more than 2 lines
poem = """\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none."""

#multiplication of string by integer
print("-"*50)
print(poem)
print("-"*50)

#string formatting with mathematical formulation
five = 10 - 2 - 6 + 3
print(f"five: {five}")

#Basic function with single argument and three return variables
def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates

#Calling/Invoking the function with variable
start_point = 10000
beans, jars, crates = secret_formula(start_point)
#Printing the result with string formatting
print("With starting point as {}".format(start_point))
print(f"We have {beans} beans, {jars} jars and {crates} crates! WooHoooo !!!")
#Printing the result with string formatting in easy way without unpacking the function return
print("We can also do this way")
start_point /= 10
pack = secret_formula(start_point)
print("We have {} beans, {} jars and {} crates! WooHoooo !!!".format(*pack))