# Inheritance
""" Usage of super method is mainly in inheritance,
if both parent and child class have their own definition of
same named function, then super will help us to use parent version
of the same method else child will use it's own function."""

class parent(object):
    def altered(self):
        print("Parent's altered()")

class child(parent):
    def altered(self):
        print("Child's altered() ")
        super(child, self).altered()
        print("Now Child is using parent's altered()")

father = parent()
son = child()

father.altered()
son.altered()
