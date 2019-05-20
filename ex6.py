# defining the variable types_of_people
types_of_people = 10

# string formatted with above variable
x = f"There are {types_of_people} types of people"

# defining the variables for strings
binary = "binary"
do_not = "don't"

# string formatted with above string variables
y = f"Those who know {binary} and those who don't {do_not}"

#print formatted string variables x and y
print(x)
print(y)

# print what I say the string variables x and y 
print(f"I said: {x}")
print(f"I also said: '{y}''")

# print the new string hilarious 
hilarious = False
joke_evaluation = "Isn't it that joke is funny?! {}"

print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."

print(w+e)