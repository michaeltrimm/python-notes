#!/usr/bin/python

"""
My name is Mike
My name is Heather
...And I am Catwoman

"""

class Person(object):
    def __init__(self, name):
        self.name = name
    
    def reveal_identity(self):
        print "My name is {}".format(self.name)
    
    def __repr__(self):
        return "Person('{}')".format(self.name)
    
    def __str__(self):
        return self.name

class SuperHero(Person):
    def __init__(self, name, hero_name):
        super(SuperHero, self).__init__(name)
        self.hero_name = hero_name
    
    def reveal_identity(self):
        super(SuperHero, self).reveal_identity()
        print "...And I am {}".format(self.hero_name)

mike = Person('Mike')
mike.reveal_identity()


heather = SuperHero('Heather', 'Catwoman')
heather.reveal_identity()
print(heather)