def spam(eggs):
    eggs.append(1)
    eggs = [2, 3]

ham = [0]
spam(ham)
print(ham)

# example 2: pass by value

def func(num):
    print("num value is:",num)
    num=50
    print("new num value is:",num)
    

a=10    
func(a)
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

--------------------------------------------
# Example 4

def test(employee):
    print("First:",employee)
    cir={'e':6,'f':9}
    employee.update(cir)
    print("final state:",employee)
    return


employee={'a':1,'b':2}
test(employee)
print(employee)    