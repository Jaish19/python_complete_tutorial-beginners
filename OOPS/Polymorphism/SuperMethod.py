class SomeBaseClass(object):
    def __init__(self):
        print('SomeBaseClass.__init__(self) called')

class UnsuperChild(SomeBaseClass):
    def __init__(self):
        print('Child.__init__(self) called')
        SomeBaseClass.__init__(self)

class SuperChild(SomeBaseClass):
    def __init__(self):
        print('SuperChild.__init__(self) called')
        super(SuperChild, self).__init__()

s = SuperChild()

print s
u = UnsuperChild()
# print "**"
print u
# print "****"

class InjectMe(SomeBaseClass):
    def __init__(self):
        print('InjectMe.__init__(self) called')
        super(InjectMe, self).__init__()

class UnsuperInjector(UnsuperChild, InjectMe): pass

class SuperInjector(SuperChild, InjectMe): pass

print "-----------------"
x = SuperInjector()
#x.mro

y = UnsuperInjector()

print "MRO.."
print SuperInjector.mro()
print UnsuperInjector.mro()





__Author__=="__Jai_Ganesh__"
Another Example for MRO



class A(object):
    def __init__(self,a,y):
        self.a=a
        self.b=y
        print("A class is called")

class B(A):
    def __init__(self):
        print("B class is called")
        A.__init__(self,3,4)

class C(A):
    def __init__(self,x,y):
        print("C is called")
        self.x=x
        self.y=y
        super(C,self).__init__(x,y)
        
    
x=C(5,4)
print(x)
y=B()
print(y)

class push(object):
    def __init__(self):
        print("Inside push")
        super(push,self).__init__()
        
class trail(C,push):
    pass
class piece(B,push):
    pass

m=trail(3,2)
n=piece()

print("Right now Method Resolution Order doing")
print(trail.mro())
print(piece.mro())