# author == 'Sanjay'

class A(object):

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return (self.a + self.b)

    def subract(self):
        return (abs(self.a - self.b))

    def something(self):
        print ("Hey this is a something function")



class firstChild(A):

    def __init__(self, x, y):

        self.x = x
        self.y = y
        super(firstChild, self).__init__(x, y)

    def multiplication(self):
        print(self.x * self.y)

    def division(self):
        print( self.x/self.y)

    # def something(self):
    #     print ("inside firstChild")

# 'Whenever we inherit A in firstChild, its not required to override all methods which Parent has.'
# 'In this above code, Add and Subract are the two methods.. ' \
# 'override only when there is a logic change, else no need to calling the method and returns nothing.'

if __name__ == '__main__':
    firstNum = int(input("enter first num"))
    secondNum = int(input("enter second num"))
    myObj = firstChild(firstNum, secondNum)
    myObj.multiplication()
    myObj.division()
    x = myObj.add()
    print (x)

    newObject = firstChild(10,10)
    newObject.something()


# 7.  Write a Python program to get the volume of a sphere with radius 6. 

class formula(object):
    def __init__(self,pi,radius):
        self.pi=pi
        self.radius=radius
        
    def calc(self):
        return 1.33*self.pi*(self.radius**2)
    

class forward(formula):
    def __init__(self,a,b):
        self.a=a
        self.b=b
        super(forward,self).__init__(a,b)
        
        
obj=forward(float(raw_input()),int(raw_input()))
print(obj.calc())

