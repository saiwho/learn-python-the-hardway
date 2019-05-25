# Animal is the object
class Animal(object):
    pass

# Dog class inherits from Animal class 
def Dog(Animal):
    def __init__(self, name):
        # Dog has a name
        self.name = name

# Cat class inherits from Animal class
def Cat(Animal):
    def __init__(self, name):
        # Cat has a name
        self.name = name

# Class Person defining here
class Person(object):
    def __init__(self, name):
        # Person has a name
        self.name = name
        # Person has a pet
        self.pet = None

class Employee(Person):
    def __init__(self, name, salary):
        # Employee has a name
        super(Employee, self).__init__(name)
        # Employee has a salary
        self.salary = salary 

# Fish is a class
class Fish(object):
    pass
# Salmon is a fish
class Salmon(Fish):
    pass
# Halibut is a fish
class Halibut(Fish):
    pass

# Rover is a dog
rover = Dog('Rover')

# satan is a cat
satan = Cat('Satan')

# Mary is a person
mary = Person('mary') 

# mary has a pet
mary.pet = satan

# Frank is a employee
frank = Employee('Frank', 10000)

# frank has a pet
frank.pet = rover

# flipper is a fish
flipper = Fish()

# Crouse is a salmon
crouse = Salmon()

# harry is a Halibut
harry = Halibut()