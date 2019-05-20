# Defining a function cheese_and_burgers
def cheese_and_burgers(no_cheese, no_burgers):
    print("You are inside cheese_and_burgers function")
    print(f"You've {no_cheese} cheese")
    print(f"You've {no_burgers} burgers")
    print("That's enough for party !\n")

# Passing integers as fn arguments
print("Passing numbers as arguments")
cheese_and_burgers(10,20)

# Passing variables as fn arguments
print("Passing variables as arguments")
no_of_cheese = 10
no_of_burgers = 20
cheese_and_burgers(no_of_cheese, no_of_burgers)

# Passing math operations as fn arguments
print("Passing math operations as fn arguments")
cheese_and_burgers(10+10, 20+20)

# Passing math operations and variables as fn arguments
print("Passing math operations and variables as fn arguments")
cheese_and_burgers(no_of_cheese+10, no_of_burgers+20)