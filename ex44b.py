# Inheritance
# Override methods Explicitly

class parent(object):
    def explicit(self):
        print("Parent explicit function")

class child(parent):
    def explicit(self):
        print("Child explicit function")

father = parent()
son = child()

father.explicit()
son.explicit()