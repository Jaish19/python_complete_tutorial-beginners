# Interview task.....data structure concepts along with memory management along with strong oops concepts...



def new_path(func):
    # Decorator method to print the operation begin...
    def wrapper(self,greet):
        func(self,greet)    
    return wrapper

def pending(func):
    
    # Decorator method to print the pending operations
    def wrapper(self,pending):
        func(self,pending)
    return wrapper

class data_base_one(object):
    
    # class data_base_one possess holds few methods with particular persons data_base
    
    def __init__(self,name,birth_date,death_date):
        self.name=name
        self._birth_date = birth_date
        self.death_date = death_date
        self.stack=[]
        
    @new_path     
    def A(self,name):
        print(name)
        print("Name: {0}  -  Birth Date: {1}  -  Death Date: {2}".format(self.name,self._birth_date,self.death_date))
        self.stack.extend([self.name,self._birth_date,self.death_date])
        return self.stack
    
    def __B(self):
        print("Name: {0}  -  Birth Date: {1}  -  Death Date: {2}".format(self.name,self._birth_date,self.death_date))
        self.stack.extend([self.name,self._birth_date,self.death_date])
        return self.stack
    
    def C(self):
        print("Name: {0}  -  Birth Date: {1}  -  Death Date: {2}".format(self.name,self._birth_date,self.death_date))
        self.stack.extend([self.name,self._birth_date,self.death_date])
        return self.stack
    
    def D(self):
        print("Name: {0}  -  Birth Date: {1}  -  Death Date: {2}".format(self.name,self._birth_date,self.death_date))
        self.stack.extend([self.name,self._birth_date,self.death_date])
        return self.stack
    
    @pending    
    def E(self,pend):
        print(pend)
        print("Name: {0}  -  Birth Date: {1}  -  Death Date: {2}".format(self.name,self._birth_date,self.death_date))
        self.stack.extend([self.name,self._birth_date,self.death_date])
        self.stack.insert(3,'Certificate pending...')
        return self.stack
        
    def _F(self):
        print("Name: {0}  -  Birth Date: {1}  -  Death Date: {2}".format(self.name,self._birth_date,self.death_date))
        self.stack.extend([self.name,self._birth_date,self.death_date])
        return self.stack
    
    def G(self):
        print("Name: {0}  -  Birth Date: {1}  -  Death Date: {2}".format(self.name,self._birth_date,self.death_date))
        self.stack.extend([self.name,self._birth_date,self.death_date])
        return self.stack
    
    def N(self):
        print("Name: {0}  -  Birth Date: {1}  -  Death Date: {2}".format(self.name,self._birth_date,self.death_date))
        self.stack.extend([self.name,self._birth_date,self.death_date])
        return self.stack
        
class data_base_two(data_base_one):
    
        # class data_base_two possess holds few methods with particular persons data_base

    
    def __init__(self,name,birth_date,death_date):
        self.name=name
        self.birth_date=birth_date
        self.death_date=death_date
        self.stack=[]
        super(data_base_two,self).__init__(self.name,self.birth_date,death_date)
        
    def __H(self):
        print("Name: {0}  -  Birth Date: {1}  -  Death Date: {2}".format(self.name,self._birth_date,self.death_date))
        self.stack.extend([self.name,self._birth_date,self.death_date])
        return self.stack
    
    def P(self):
        print("Name: {0}  -  Birth Date: {1}  -  Death Date: {2}".format(self.name,self._birth_date,self.death_date))
        self.stack.extend([self.name,self._birth_date,self.death_date])
        return self.stack
    
    @pending
    def I(self,pend):
        print(pend)
        print("Name: {0}  -  Birth Date: {1}  -  Death Date: {2}".format(self.name,self._birth_date,self.death_date))
        self.stack.extend([self.name,self._birth_date,self.death_date])
        return self.stack
    
    def J(self):
        print("Name: {0}  -  Birth Date: {1}  -  Death Date: {2}".format(self.name,self._birth_date,self.death_date))
        self.stack.extend([self.name,self._birth_date,self.death_date])
        return self.stack
    
    def K(self):
        print("Name: {0}  -  Birth Date: {1}  -  Death Date: {2}".format(self.name,self._birth_date,self.death_date))
        self.stack.extend([self.name,self._birth_date,self.death_date])
        return self.stack
    
    def L(self):
        print("Name: {0}  -  Birth Date: {1}  -  Death Date: {2}".format(self.name,self._birth_date,self.death_date))
        self.stack.extend([self.name,self._birth_date,self.death_date])
        self.stack.pop()   # pop the last element from the stack
        print("Length of L stack is:",len(self.stack)) # finding the length of the stack
        return self.stack
    
    def M(self):
        print("Name: {0}  -  Birth Date: {1}  -  Death Date: {2}".format(self.name,self._birth_date,self.death_date))
        self.stack.extend([self.name,self._birth_date,self.death_date])
        return self.stack
    
    def O(self):
        print("Name: {0}  -  Birth Date: {1}  -  Death Date: {2}".format(self.name,self._birth_date,self.death_date))
        self.stack.extend([self.name,self._birth_date,self.death_date])
        return self.stack
    

    
class data_base_three(data_base_two,data_base_one):
    
#     Multiple Inheritance...with method resolution order....
    
    def __init__(self,name,birth_date,death_date):
        self.name=name
        self.birth_date=birth_date
        self.death_date=death_date
        super(data_base_three,self).__init__(self.name,self.birth_date,self.death_date)
        
    def Q(self):
        print("Name: {0}  -  Birth Date: {1}  -  Death Date: {2}".format(self.name,self._birth_date,self.death_date))
        self.stack.extend([self.name,self._birth_date,self.death_date])
        return self.stack
    
    def R(self):
        print("Name: {0}  -  Birth Date: {1}  -  Death Date: {2}".format(self.name,self._birth_date,self.death_date))
        self.stack.extend([self.name,self._birth_date,self.death_date])
        return self.stack
    
    def S(self):
        print("Name: {0}  -  Birth Date: {1}  -  Death Date: {2}".format(self.name,self._birth_date,self.death_date))
        self.stack.extend([self.name,self._birth_date,self.death_date])
        return self.stack
    
    def T(self):
        print("Name: {0}  -  Birth Date: {1}  -  Death Date: {2}".format(self.name,self._birth_date,self.death_date))
        self.stack.extend([self.name,self._birth_date,self.death_date])
        return self.stack
    
    def U(self):
        print("Name: {0}  -  Birth Date: {1}  -  Death Date: {2}".format(self.name,self._birth_date,self.death_date))
        self.stack.extend([self.name,self._birth_date,self.death_date])
        return self.stack
    
    def V(self):
        print("Name: {0}  -  Birth Date: {1}  -  Death Date: {2}".format(self.name,self._birth_date,self.death_date))
        self.stack.extend([self.name,self._birth_date,self.death_date])
        return self.stack
    
    def unknown(self):
        print("Name: {0}  -  Birth Date: {1}  -  Death Date: {2}".format(self.name,self._birth_date,self.death_date))
        self.stack.extend([self.name,self._birth_date,self.death_date])
        return self.stack
        


p1=data_base_one('Mr.A',1685,1999)
p2=data_base_one('Mr.B',1485,1555)
p3=data_base_one('Mr.C',1478,1520)
p4=data_base_one('Mr.D',1479,1500)
p5=data_base_one('Ms.E',1987,2054)
p6=data_base_one('Mrs.F',1564,1655)
p7=data_base_two('Mrs.G',1992,2064)
p8=data_base_two('Mrs.H',1992,2098)
p9=data_base_two('Mrs.I',1855,1955)
p10=data_base_two('Mrs.J',1877,2088)
p11=data_base_two('Mrs.K',1855,2077)
p12=data_base_two('Mrs.L',1588,1788)
p13=data_base_three('Mrs.M',1991,2066)
p14=data_base_three('Mrs.N',2000,2099)
p15=data_base_three('Mrs.O',1554,1656)
p16=data_base_three('Mrs.P',1588,2066)
p17=data_base_three('Mr.Q',1685,1999)
p18=data_base_three('Mr.R',1485,1555)
p19=data_base_three('Mr.S',1478,1520)
p20=data_base_three('Mr.T',1479,1500)
p21=data_base_three('Ms.U',1987,2054)
print(" Stack Value of A is:",p1.A("Operation Begins..."))
print(" Stack Value of B is:",p2._data_base_one__B())
print(" Stack Value of C is:",p3.C())
print(" Stack Value of D is:",p4.D())
print(" Stack Value of E is:",p5.E("Certification pending process..."))
print(" Stack Value of F is:",p6._F())
print("Stack Value of G is:",p7.G())
print("Stack Value of H is:",p8._data_base_two__H())
print("Stack Value of I is:",p9.I("Process pending..."))
print(" Stack Value of J is:",p10.J())
print(" Stack Value of K is:",p11.K())
print(" Stack Value of L is:",p12.L())
print(" Stack Value of M is:",p13.M())
print(" Stack Value of N is:",p14.N())
print(" Stack Value of O is:",p15.O())
print(" Stack Value of P is:",p16.P())

print(" Stack Value of Q is:",p17.M())
print(" Stack Value of R is:",p18.N())
print(" Stack Value of S is:",p19.O())
print(" Stack Value of T is:",p20.P())
print(" Stack Value of U is:",p21.P())

# Generator function

def logic():
    for i in range(2,4):
        a,b,c=raw_input("Enter the name:"), int(raw_input("Birth_date:")), int(raw_input("Death_date:"))
        yield a,b,c  # Generator method

c=logic()
for i in c:
    p22=data_base_three(i[0],i[1],i[2])
    print(" Stack Value of V is:",p22.unknown())




