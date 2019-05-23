from sys import exit

# Gold room fn definition 
# Called from bear_room
def gold_room():
    print("Room is full of gold")
    print("How much do you take ?")
    # Taking the option
    option = int(input('> '))
    if option>=50:
        # Calling the dead function if too greedy
        print("You are too much greedy")
        dead("You'll be crushed due to greedy!")
    elif option < 50:
        # If not so greedy then Game Over
        print("Thats good ! You've took it suffiecient")
        print("Game Completed")
        exit(0)
    else:
        # If nothing has been given then ask user again for option
        print("Type some number instead of nothing")
        option = int(input('> '))

# bear_room fn definition
# Called from start() fn if user choses left door
def bear_room():
    print("Bear is there inside the room")
    print("Bear is covering the door")
    print("Bear is catching some honey")
    print("How are you going to move the bear ?")
    print("options are take honey, taunt, open door")
    # Initially bear in front of the door so False
    bear_moved = False

    # Infinite loop breaks when conditions are satisfied
    # 1. take honey -> dead fn is called and the loop breaks
    # 2. taunt -> bear will move and now we can easily open our door
    # 3. open door -> Initially open door doesn't open as bear moved is False, so use taunt and then open door
    # 4. else is if you give other than above three options 
    while True:
        option = input('> ')

        if option == 'take honey':
            dead("Bear looks at you slaps off your face")
        elif option == "taunt" and not bear_moved:
            print("Go through the door as beared moved off")
            bear_moved = True
        elif option == "taunt" and bear_moved:
            print("Bear pissed off and eats your hands")
        elif option == "open door" and bear_moved:
            gold_room()
        else:
            print("You should select some option stupid")

# Cthulhu_room() fn definition
# Called from start() fn if user chooses right door
def cthulhu_room():
    print("Here you see the great evil Cthulhu.")
    print("He, it, whatever stares at you and you go insane.")
    print("Do you flee for your life or eat your head?")
    choice = input("> ")
    # flee starts the game again
    if "flee" in choice:
        start()
    # head makes the cthulhu eats the user head and make him dead using dead fn
    elif "head" in choice:
        dead("Well that was tasty!")
    # If other option then same fn is invoked to ask relevant action
    else:
        cthulhu_room()

# Dead fn definition
# Called from bear room fn, cthulhu fn, gold room fn and start function
    print(why, "Good job!")
    print("Game Over !")
    exit(0)

# start fn definition
# This is the starting point to the puzzle
def start():
    print("The puzzle game is going to be started !S")
    print("You are in a dark room.")
    print("There is a door to your right and left.")
    print("Which one do you take?")
    choice = input("> ")
    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")

# Starts the game after start() is called 
start()