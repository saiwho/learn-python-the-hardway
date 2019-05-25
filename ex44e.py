# Composition is another way of doing the work of inheritance 
# Same as before exercise but implementing via composition

class Other(object):
    def implicit(self):
        print('Other\'s implicit()')
    
    def override(self):
        print('Other\'s explicit()')

    def altered(self):
        print('Other\'s altered()')    

class Child(object):
    def __init__(self):
        self.other = Other()

    def implicit(self):
        self.other.implicit()

    def override(self):
        print('Child\'s explicit()')

    def altered(self):
        print('Child\'s altered()')
        print('Now implementing Other\'s altered() via Child, This is same as super function functioning')
        self.other.altered()
        print('Now both Other\'s and Child\'s altered function succesfully implemented')
    
son = Child()
son.implicit()
son.override()
son.altered()
        