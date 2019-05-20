print("Puzzle starts")
print("""You entered the dark room with two doors. Which
            door you want to continue""")

door = input('> ')

if door == '1':
    print("There's a giant bear here eating a cheese cake.")
    print("What do you do?")
    print("1. Take the cake.")
    print("2. Scream at the bear.")

    bear = input('> ')

    if bear == '1':
        print("Bear eats off your face")
    elif bear == '2':
        print("Bear eats off your hands and legs")
    else:
        print(f"Doing {bear} is better")
        print("Bear runs off from there")

elif door == '2':
    print("You stare into the endless abyss at Cthulhu's retina.")
    print("1. Blueberries.")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling melodies.")

    option = input('> ')

    if option == '1'or option == '2':
        print("Your body survives powered by a mind of jello.")
        print("Good job!")
    else:
        print("The insanity rots your eyes into a pool of muck.")
        print("Good job!")
else:
    print("""You stumble around and fall on a knife and die.
    Good job!""")
print("Puzzle complete")