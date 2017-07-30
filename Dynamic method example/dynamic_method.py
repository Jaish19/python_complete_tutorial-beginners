# Given the dynamic nature of Python you can do many things in runtime, like add methods dynamically to an object or class. 
# This is particularly useful when writing unit tests.

# Here is the simplest way, adding a method to and object:

class Person(object):
    pass


def play():
    print "i'm playing!"



p = Person()
p.play = play
p.play()

--------------------------------------------------------------------------------------
# note that play is just a function, it doesn't receive self. There is no way to 
# p knows that it's a method. If you need self, you must create a method and then bind to the object:

from types import MethodType


class Person(object):
    def __init__(self, name):
        self.name = name



def play(self):
    print "%s is playing!" % self.name



p = Person('jai')
p.play = MethodType(play, p)
p.play()

-------------------------------------------------------------------------------------------------\
# In these examples, only the p instance will have play method, other instances of Person won't. To accomplish this we need to add the method to the class:

class Person(object):
    def __init__(self, name):
        self.name = name


def play(self):
    print "%s is playing!" % self.name



Person.play = play



p1 = Person("igor")
p1.play()



p2 = Person("joh")
p2.play()


# note that we don't need to create a method with types.MethodType here, because all functions in the body 
# of a class will become methods and receive self, unless you explicit say it's a classmethod or staticmethod.

------------------------------------------------------------------------------------------
# Python doesn't allow to add methods to built-in types, actually to any type defined in C. 
# The unique way around this is to subclass the type, here is an example:


class UpperList(list):
    pass


def to_upper(self):
    for index, item in enumerate(self):
        self[index] = item.upper()



UpperList.to_upper = to_upper



l = UpperList(['i','g','o','r'])
l.to_upper()
print l

----------------------------------------------------------------------------------