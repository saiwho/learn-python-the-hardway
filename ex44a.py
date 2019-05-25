# Inheritance 
# Overide methods Implicitly
# Action child means action on parent

class parent(object):
    def implicit(self):
        print("Implicit funtion of parent class")

class child(parent):
    pass

father = parent()
son = child()

father.implicit()
son.implicit()