# GENERATORS:
# Generators simplifies creation of iterators. A generator is a function that produces a sequence of results 
# instead of a single value.

def foo():
    print "begin"
    for i in range(3):
        print "before yield", i
        yield i
        print "after yield", i
    print "end"

f=foo()
for i in range(f):
	print(i)



# EXAMPLE 2

def integers():
    """Infinite sequence of integers."""
    i = 1
    while True:
        yield i
        i = i + 1

def squares():
    for i in integers():
        yield i * i
def norms():
    return 1

def take(n, seq):
    """Returns first n values from the given sequence."""
#     seq = iter(seq)
#     print(seq)
    result = []
    try:
        for i in range(n):
            result.append(seq.next())
    except StopIteration:
        pass
    return result

print take(5, squares()) # prints [1, 4, 9, 16, 25]

# EXAMPLE 3

import random

def lottery():
    # returns 6 numbers between 1 and 40
  for i in range(6):
    yield random.randint(1, 40)

    # returns a 7th number between 1 and 15
    yield random.randint(1,15)

for random_number in lottery():
       print("And the next number is... ",  )



# EXAMPLE FOR FIBONACCI SERIES USING GENERATORS

def flow():
    i=1
    while True:
        yield i
        i+1
    
     
def operation():
    n1=0
    n2=1
    for i in flow():
        nth=n1+n2
        yield nth
        n1=n2
        n2=nth
        

def fib(n,jai):
    result=[]
    for i in range(n):
        result.append(jai.next())
        
    return result

    
        
print(fib(10,operation()))





















