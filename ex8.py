#defining the formatter string variable for formatting
formatter = "{} {} {} {}"

#formatting with integers
print(formatter.format(1, 2, 3, 4))
#formatting with strings
print(formatter.format("one", "two", "three", "four"))
#formatting with boolean values
print(formatter.format(True, False, False, True))
#formatting with itself i.e print itself as output
print(formatter.format(formatter, formatter, formatter, formatter))
#formatting with big strings
print(formatter.format("Try your", "Own text here", "May be a poem", "Or a song about fear"))
