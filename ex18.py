# This way of defining a function is nothing but unrolling funciton parameters
# Commonly we don't do this 
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

# This way of defining the same function is commonly used i.e.., directly parameters are used
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

# Takes only one argument
def one_arg(arg1):
    print(f"arg1: {arg1}")

#This function don't take any arguments
def none_arg():
    print("Takes no arguments")

print_two("Sai", "Pothan")
print_two_again("Sai", "Pothan")
one_arg("Sai")
none_arg()