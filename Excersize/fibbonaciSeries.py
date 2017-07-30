num = 20
n1=0
n2=1
camp=[]
for i in range(num+1):
    nth=n1+n2
    camp.append(nth)
    n1=n2
    n2=nth
print(camp)



# FIBONACCI SERIES USING GENERATOR OPERATION

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
