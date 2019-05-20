from sys import argv

script, user_name = argv
prompt = '--> '

print(f"Hi {user_name}, I'm the {script}")
print("I would like to ask few questions")

print(f"Do you like me {user_name} ?")
likes = input(prompt)

print(f"Where do you live {user_name} ?")
place = input(prompt)

print(f"What is the name of your computer {user_name} ?")
pc_name = input(prompt)

#Both gives same output
print(f"""So, You said {likes} about liking me, you live in {place} and your computer name is {pc_name}""")
print("""So, You said {} about liking me, you live in {} and your computer name is {}""".format(likes, place, pc_name))