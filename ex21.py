# fn to add two numbers
def add(a,b):
    print(f"Adding {a} + {b}")
    return a+b

# fn to subtract two numbers
def subtract(a,b):
    print(f"Subtracting {a} - {b}")
    return a-b

# fn to divide two numbers
def divide(a,b):
    print(f"Division {a}/{b}")
    return a/b

# fn to multiply two numbers
def multiply(a,b):
    print(f"Multipying {a}*{b}")
    return a*b

print("Let's do some math using functions:")

# Doing some mathematical operations using written functions
a = add(30,5) #35
b = divide(100,2) #50
c = multiply(90,2) #180
d = subtract(78,4) #74
# Priting the results 
print(f"a = {a}, b = {b}, c = {c}, d = {d}")

# A small puzzle from the book 
print("Now a puzzle")
w = add(a, subtract(d, multiply(c, divide(b,2)))) #25*180-74+35
ww =  a+d-c*(b/2) 
# formula -> P*R*T/100 , function -> divide(multiply(multiply(P,R),T), 100)  ----- This is the example
print(f"The answer to the puzzle is {w} by functions & {ww} by formula written")