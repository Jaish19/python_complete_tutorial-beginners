------------------------------------------------INTERVIEW QUESTIONS---------------------------------------------

# VALIDATION OF IP ADDRESS
def InternetProtocol(val):
    address={'ip1':'192.168.10.1',
             'ip2':'10.10.1.0'}
    for k,v in address.items():
        if val==v:
            print("yeah!!Its valid ip address",val)
        else:
            pass
        
        
InternetProtocol(str(raw_input("Enter the IP address here:")))

--------------------------------------------------------------------------------

# VALIDATING THE IP IPV4 AND IPV6 IP ADDRESS


import socket

def is_valid_ipv4_address(address):
    try:
        socket.inet_pton(socket.AF_INET, address)
    except AttributeError:  # no inet_pton here, sorry
        try:
            socket.inet_aton(address)
        except socket.error:
            return False
        return address.count('.') == 3
    except socket.error:  # not a valid address
        return False

    return True

def is_valid_ipv6_address(address):
    try:
        socket.inet_pton(socket.AF_INET6, address)
    except socket.error:  # not a valid address
        return False
    return True


print(is_valid_ipv4_address('12.18.10.1'))
# print(is_valid_ipv6_address('2001:0db8:85a3:0000:0000:8a2e:0370:7334'))


--------------------------------------------------------------------------------------------------------


# DAY,MONTH AND YEAR

class Calender(object):
    def __init__(self,one):
        self.one=one
    def logging(self):
        cat=[]
        for i in range(len(self.one)):
            cat.append(self.one[i])
        return cat

obj=Calender(map(int,raw_input("Enter the day and date with year:").split(' ')))
c=obj.logging()
print("Day:",c[0],"Month:",c[1],"Year:",c[2])


---------------------------------------------------------------------------------------------------



# INHERITANCE CONCEPT


class Father(object):
    def __init__(self):
        pass

    def getUpEarlyMorning(self):
        print("Get up Early at 6 AM")


class Mother(object): # please don't mind the name of the class

    def __init__(self):
        pass

    def getUpEarlyMorning(self):
        print("Get up Early at 4 AM")


class ChildClass(Mother, Father):  # Method resolution order
    # Child is ready to listen both Mother and Father behaviour, but priority goes to mom first.
    # Because, we are inheriting "Mother" first. (Method Resolution Order)
    def __init__(self):
        pass

    def getUpEarlyMorning(self):
        print("I will get up at 5 AM")
        # pass

if __name__ == '__main__':
    b = ChildClass()
    b.getUpEarlyMorning()
    print (ChildClass.__mro__)


   -----------------------------------------------------------------------------------------------


   class main(object):
    def go(self):
        print("Go main Go")
    def pause(self):
        print("Go Pause main go")
class A(main):
    def go(self):
        super(A,self).go()
        print("Go A Go")
    def pause(self):
        print("Go Pause A go")
        
class B(A):
    def go(self):
        super(B,self).go()
        print("Go B Go")
    def pause(self):
        print("Go Pause B go")
        
        
a=A()
b=B()
b.go() 







  ---------------------------------------------------------------------------------



  # DICTIONARY METHODS

  c={i:i*i for i in range(10)}
k=[[i,i*i] for i in range(10)]
print(k)
for i in range(len(k)):
    print(dict(zip(k[i],k[i+1])))


----------------------------------------
c={i:i*i for i in range(10)}
# only key will be print

for i in c:
    print(i)
# only value will be print

for i in c:
    print(c[i])
    
# another method(both key and value will be print here, though another variable is not defined)

for i in c.iteritems():
    print(i)
    
    
# another method

for i,j in c.iteritems():
    print(i,j)


 ----------------------------------------------------------------------------


 # PEP 8

 # When you develop a program in a group of programmers, it is really important to follow some standards. 
 # If all team members format the code in the same prescribed format, then it is much easier to read the code. 
 # For the same purpose pep8 is used to ensure python coding standards are met.



 ==========================================================================================
 --------------------HCL INTERVIEW QUESTIONS-------------------------------------------
 ==========================================================================================
 # 1. How to call the private methods from packages 

 # EG:1:this is from outside the packages

 from module.mul import * # 'module' means its a folder and 'mul.py' is file name and '*' is to call all the methods from the 'mul.py'

obj=multiply(5,4)
obj._multiply__mixer()

#Eg: 2 this is to call private method from the __sub.py (if we mention 'import *' it will not work...so we need to mention the particular private method while importing.)

from module.__sub import __difference # never work if 'from module.__sub import *'

__difference(5,4)

-------------------------------------------------------------------------------------------

# create the filename.txt and write some txt into it...if that file already exist means just print its already exist

# METHOD 1:
import os
if os.path.exists('filename.txt'):
    print "File exists"

else:
    
     with open("filename.txt", 'w+') as fr:
       fr.write("new gen")
       
with open("filename.txt","r") as fw:
    print(fw.read(5))



# GREAT METHOD 2


import os

def create():
    
    try:
        print(os.getcwd())
        os.mkdir("E:\gum")
        print(os.getcwd())
        os.chdir("E:\gum")
        print(os.getcwd())
        if os.path.exists("filename.txt"):
            print("Its already exist")
        else:
            with open("filename.txt",'w') as fw:
                fw.write("welcome new checking operation")
        
    except:
        print("Cant handle this operation until gets corrected")
        
        
create()

---------------------------------------------------------------------------------------------------------------
# THROWING ERRORS THROUGH ANOTHER FUNCTION:

import os
def main():
    print("this file may exist already")
    
def create():
    try:
        print(os.getcwd())
        os.chdir("./fund")
        print(os.getcwd())
        name=raw_input("User type the file name you wanna create:")+".txt"
        if os.path.exists(name):
            main()
        else:
            with open(name,'w') as fw:
                fw.write("Hi I am moving towards success")
                
    except:
        print("Techii fault")
        
        
create()

----------------------------------------------------------------------------------------------------



# addtion of two list via parellel and sum of it

# METHOD 1

a=[1,2,3]
b=[4,5,6]
l=[]
[l.append(a[i]+b[i]) for i in range(len(a))]
   
print(sum(l))

# METHOD 2:

a=[1,2,3]
b=[4,5,6]

c=[a[i]+b[i] for i in range(len(a))]
   
print(sum(c))

----------------------------------------------------------------------------------------------------


# INSTANCE ATTRIBUTES AND DYNAMIC ATTRIBUTES:



class person():
    def __init__(self,age,salary):
        self.age=age 
        self.salary=salary
    
class experience():
    def __init__(self,experience):
        self.experience=experience
        print("The experience state is:",self.experience)
        
        
exp=[1,2,3,4,5,6]
person(15,8000)
# for i in exp:
#     experience(i)
for i in range(int(raw_input("User how many times you wanna iterate:"))):    
    experience(raw_input("user please enter the experience:"))


---------------------------------------------------------------------------------------------

# MAPPING:

# map(function_to_apply, list_of_inputs)

# # The map function is the simplest one among Python built-ins used for functional programming. 
# These tools apply functions to sequences and other iterables. The filter filters out items based on a test 
# function which is a filter and apply functions to pairs of item and running result which is reduce.

------------------------------------------------------------------------------------------------------------------

# CONVERT DECIMAL TO BINARY VALUE


def convertToBinary(n):
   """Function to print binary number
   for the input decimal using recursion"""
   if n > 1:
       convertToBinary(n//2)
   cal=n % 2
   u=' '
   print(" ".join())

# decimal number
dec = 34

convertToBinary(dec)

# TYPE 2:

from __future__ import print_function
a = int(raw_input())
s = []
for i in range(1, (a+1)):
    s.append(str(i))
    
print("".join(s))

---------------------------------------------------------------------------------------------------------

# ARMSTRONG NUMBER

# num = int(input("Enter a number: "))

# initialize sum
sum = 0
num=153
# find the sum of the cube of each digit
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** len(str(num))
   temp //= 10

# display the result
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")

----------------------------------------------------------------------------------------------------

# LOCAL AND GLOBAL VARIABLES

def fun1(a):
            print 'a:', a
            a= 33;
            print 'local a: ', a
a = 100
fun1(a)
print 'a outside fun1:', a
def fun2():
            global b
            print 'b: ', b
            b = 33
            print 'global b:', b
b =100
fun2()
print 'b outside fun2', b

-------------------------------------------------------------------------------------------------

# Dynamic method example code---detail code refer dynamic_method folder


class Person(object):
    pass


def play():
    print "i'm playing!"



p = Person()
p.play = play
p.play()


----------------------------------------------------------------------------

# LOCAL AND GLOBAL VARIABLES(MERIT SOFTWARES)

def f(): 
    print s 
s = "I hate spam"
f()

2.

def f(): 
    s = "Me too."
    print s 

s = "I hate spam." 
f()
print s

--------------------------------------------------------------------------------

# HOW TO EXTRACT NUMBER FROM THE STRING(MERIT SOFTWARES)

val="h25ello mike test 1 2 3"
print(val.split())
for s in val.split():f
#     print(s)
    if s.isdigit():
        print(s) 
    else:
        pass

------------------------------------------------------------------

# what is lambda?(MERIT SOFTWARES)

In python, lambda is anonyms function is a function that is defined without name. 
while normal functions are defined using the def keyword.


--------------------------------------------------------------------------
# how do you iterate over a list and pull element indices at the same time?


my_list = ['a', 'b', 'c']
print(list(enumerate(my_list)))

-----------------------------------------------------------------
# LIST COMPREHENSION

# Python: List Comprehensions. ... Everything else is output from Python. Python supports 
# a concept called "list comprehensions". It can be used to construct lists in a very natural, 
# easy way, like a mathematician is used to do.

# DICTIONARY COMPREHENSION

# You can use dict comprehensions in ways very similar to list comprehensions, 
# except that they produce Python dictionary objects instead of list objects.


-------------------------------------------------------------------------------------------
# How to search the words and replacing it using file HANDLING

METHOD 1:

import fileinput
userFile=raw_input("Enter the file name:")+'.txt'
textToSearch=raw_input("Enter the search word:")
textToCorrect=raw_input("Enter to correct:")
# print(userInput)
with open(userFile,'r+') as fr:
    
    for line in fileinput.input(userFile):
        fr.write(line.replace(textToSearch,textToCorrect))

METHOD 2:

with open('read.txt','r+') as file:
    filedata=file.read()
    filechange=filedata.replace('Internet','Online')

with open('read.txt','w') as file:
    file.write(filechange)


METHOD 3: COUNT OF LETTERS


with open('read.txt','r+') as file:
    filedata=file.read()
print(filedata.count('a'))

--------------------------------------------------------------------------------------


# Read a txt file and do the changes and copy the changed informations to new txt file

with open('read.txt', 'r') as file :
  filedata = file.read()

# Replace the target string
filedata = filedata.replace('Internet', 'Online')
print(filedata.count('a'))

# Write the file out again
with open('state.txt', 'w') as file:
  file.write(filedata)

----------------------------------------------------------------------------------

# WRITE THE ANSWER FOR BELOW QUESTION:

class Node(object):
    def __init__(self,sName):
        self._lChildren=[]
#         print(self._lChildren)
        self.sName=sName
    def __repr__(self):
        return "<Node'{}'>".format(self.sName)
    def append(self,*args,**kwargs):
        self._lChildren.append(*args,**kwargs)
        # print(self._lChildren)
    def print_all_1(self):
        print(self)
        for oChild in self._lChildren:
            oChild.print_all_1()
            
    def print_all_2(self):
        def gen(o):
            lAll=[o,]
            while lAll:
                oNext=lAll.pop(0)
                lAll.extend(oNext._lChildren)
                yield oNext
        for oNode in gen(self):
            print(oNode)
            
            
            
oRoot=Node("root")
oChild1=Node("child1")
oChild2=Node("child2")
oChild3=Node("child3")
oChild4=Node("child4")
oChild5=Node("child5")
oChild6=Node("child6")
oChild7=Node("child7")
oChild8=Node("child8")
oChild9=Node("child9")
oChild10=Node("child10")


oRoot.append(oChild1)
oRoot.append(oChild2)
oRoot.append(oChild3)
oChild1.append(oChild4)
oChild1.append(oChild5)
oChild2.append(oChild6)
oChild4.append(oChild7)
oChild3.append(oChild8)
oChild3.append(oChild9)
oChild6.append(oChild10)

oRoot.print_all_1()
oRoot.print_all_2()

# OUTPUT:


<Node'root'>
<Node'child1'>
<Node'child4'>
<Node'child7'>
<Node'child5'>
<Node'child2'>
<Node'child6'>
<Node'child10'>
<Node'child3'>
<Node'child8'>
<Node'child9'>
<Node'root'>
<Node'child1'>
<Node'child2'>
<Node'child3'>
<Node'child4'>
<Node'child5'>
<Node'child6'>
<Node'child8'>
<Node'child9'>
<Node'child7'>
<Node'child10'>



---------------------------------------------------------------------------------------


# ABOVE QUESTION UNDERSTANDABLE FORMAT:

class Node(object):
    def __init__(self,Name):
        self._Children=[]

        self.Name=Name
        
    def __repr__(self):
        return "<Node'{}'>".format(self.Name)
    
    def append(self,*args,**kwargs):
        self._Children.append(*args,**kwargs)
        print(self._Children)
        
    def print_all_1(self):
        print(self)
        print(self._Children)
        for Child in self._Children:
            Child.print_all_1()
            
    def print_all_2(self):
        print(self)
        def gen(o):
            print(o)
            All=[o,]
            while All:
                print(All)
                Next=All.pop(0)
                print(Next)
                All.extend(Next._Children)
                print(Next._Children)
                yield Next
        for Node in gen(self):
            print(Node)
            
            
            
Root=Node("root")
Child1=Node("child1")
Child2=Node("child2")
Child3=Node("child3")
Child4=Node("child4")
Child5=Node("child5")
Child6=Node("child6")
Child7=Node("child7")
Child8=Node("child8")
Child9=Node("child9")
Child10=Node("child10")


Root.append(Child1)
Root.append(Child2)
Root.append(Child3)
Child1.append(Child4)
Child1.append(Child5)
Child2.append(Child6)
Child4.append(Child7)
Child3.append(Child8)
Child3.append(Child9)
Child6.append(Child10)

Root.print_all_1()
Root.print_all_2()


-------------------------------------------------------------------

what is difference between range and arange?

arange: Return evenly spaced values within a given interval.

For integer arguments the function is equivalent to the Python built-in range function, 
but returns an ndarray rather than a list.



import numpy as np
print(np.arange(10.2))
print(np.arange(10))

----------------------------------------------------------------------------
creating the multi-dimensional array:
TYPE_1:

a=[[] for _ in range(5)]
print(a)

TYPE_2:

a=[]
a.append([])
a[0].append('aa1')
a[0].append('aa2')
print(a)

TYPE_3:

a=[[] for _ in range(5)]
a[0].append('aa1')
a[1].append('aa2')
a[2].append('aa3')
print(a)

TYPE_4:

arr = [[]]*3 
print(arr)

TYPE_5:

print("Enter the value of x: ")
 x=int(raw_input())

 print("Enter the value of y: ")
 y=int(raw_input())
z=[[0 for row in range(0,x)] for col in range(0,y)]
print(z)

TYPE_6:

import numpy
print(numpy.matrix([[1,2],[5,4]]))
print(numpy.matrix('1 2; 3 4'))
print(numpy.arange(25).reshape((5, 5)))
print(numpy.array(range(25)).reshape((5, 5)))


TYPE_7: EASY METHOD TO CREATE AN array

import numpy
print(numpy.zeros((5,5)))
print(np.ones((5,5)))

5 rows & 10 columns easy way:

arr = eval('[[0]*5]*10')
print(arr)

TYPE_8: DIFFERENCE BETWEEN ARRAY AND LIST

import numpy
x = numpy.array([3, 6, 9, 12])
# x=[3,6,9,12]
z=x/3.0
print(z)


-------------------------------------------------------------------
sum the numbers using list comprehension

l1=[1,2,3,4,5]

l3=[i for i in l1 if l1.index(i)<len(l1)]
print(sum(l3))


TYPE 2:

print(reduce(lambda x,y:x+y,l1))

------------------------------------------------------------------

LIST COMPREHENSION EXAMPLE:

set_words="The way we follow will help us to grow to achieve some thing in our life"
words=set_words.split()
print(words)        
stuff=[[i.upper(), i.lower(), len(i)]for i in words]
for i in stuff:
    print(i)


-----------------------------------------------------------------------

# class instance and instance variable

class abc():
    a=2
    def __init__(self,b):
        self.b=b
        
        
wit=abc(4)
jus=abc(6)
print(wit.a)
print(wit.b)
print(jus.b)

===========================================================================================

------------------------------------------------------
# example: pass by value --- best examples

def delimeter(x):
    x=45 # actual value
    print(x)
    
    
x=15
delimeter(x) #here we passing the copied value of x not actual value...so it will not affect the outside function...
print(x)

# example 3 pass by reference - best examples

def func(num):
    print("num value is:",num)
    num[0]=9
    num[1]=8
    print("new num value is:",num)
    return
    

a=[1,2,3,4,5]    
func(a) # in this case of call by reference, we are passing actual list not a copied list to inside function...it will reflect inside the function as well as outside the function 
print(a)

---------------------------------------------------------------------------------------------

# To check numeric is existing in file or not

with open('fine.txt','r+') as fo:
    for i in fo.read().split():
        if i.isdigit():
            print("yes numeric is existing here",i)
        else:
            pass
--------------------------------------------------------------------




DATA STRUCTURE CONCEPT WITH STRONG OOPS METHODS...


# Interview task.....strong data structure with memory management methods along with strong oops concepts...



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




===================================================================================================




