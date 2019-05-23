fruits = {'apples': 'I am apples'}

def apples():
    print('I am apples')

tangerine = 'Living reflection of dream'

"""Python works on the principle of Dictionaries i.e.., Key - Value pair i.e get
                    something out of it using key's name"""

# importing modules and calling them via . operator import ex40a -> ex40a.apples()
# Variable calling -> ex40a.tangerine
# dictionary calling are similar but change in syntax -> fruits['apples']
# Dictionary -> Key is string
# class -> .something is the key also know as dot operator or identifier

class apples():
    def __init__(self):
        self.tangerine =  'Living reflection of dream'
    def apples(self):
        print('I am apples')

#Class Style
objectapple = apples()
objectapple.apples()
print(objectapple.tangerine)

#Dict style
print(fruits['apples'])

#module style 
apples()
print(tangerine)