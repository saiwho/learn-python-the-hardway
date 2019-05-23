# Defining the string
ten_string = "cake cookie bun orange fire"
# Splitting the string into list items
ten_things = ten_string.split(' ')
print("This list is not containing 10 things\nLet's add them")
# Defining the another_list list
another_list = ["baby", "coke", "pepsi", "donkey", "tiger", "can"]

# Appending another list items to ten_things list
while len(ten_things) != 10:
    add_item = another_list.pop()
    print(f"There are {len(ten_things)} items in the list")
    print(f"Adding {add_item} to the ten_things list")
    ten_things.append(add_item)

print("Wow Now ten things are there in ten_things list")
# Printing all the items of the list
print(ten_things)
# This give the second item which is ordinal and 1 is cardinal
print(ten_things[1])
# ten_things[-1] gives the last item of the list
print(ten_things[-1])
# pop usually gives the last item of the list
print(ten_things.pop())
# Important stuff 
# join joins the list items into a string using delimiter as ' ' or # or anything we pass
print(' '.join(ten_things)) # what? cool!
print('#'.join(ten_things[3:5])) # super stellar!