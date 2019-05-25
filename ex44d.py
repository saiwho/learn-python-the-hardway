class parent(object):
    
    # Implicit calling
    def implicit(self):
        print('parent implicit()')
    
    # Explicit or override
    def explicit(self):
        print('parent explicit()')
    
    # altered i.e using super method
    def altered(self):
        print('parent altered()')

class child(parent):

    # child version of explicit method
    def explicit(self):
        print('child explicit()')

    #usage of super method 
    def altered(self):
        print('child altered()')
        print('Now using super method to get same function defined in parent class')
        super(child, self).altered()
        print('after using parent version of same function, continued here')

father = parent()
son = child()


print('-'*60)
print('Implicit calling')
print('-'*60)
father.implicit()
son.implicit()
print('\n')

print('-'*60)
print('Explicit calling or overriding')
print('-'*60)
father.explicit()
son.explicit()
print('\n')

print('-'*60)
print('Usage of super() method')
print('-'*60)
father.altered()
son.altered()
