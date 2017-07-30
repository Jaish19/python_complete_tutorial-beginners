def square(x):
    return x**2

if __name__ == '__main__':
    print(square(10))

    l1 = [1,2,4,5,654,5,65,778]
    # for i in l1:
    #     print(square(i),end=" ")

    l2 = [None]*len(l1)
    print (l2)

    l3 = (list(map(square, [1,2,4,5,654,5,65,778])))
    l4 = range(len(l1))

    print(dict(zip(l3,l2)))

    from functools import reduce
    # print(list(lambda x,y -> x*y))
    print(list(map(lambda x,y: x*y, l1, l4)))

    print(filter(lambda x: x%2==0, [1,2,3,5]))

    reduce(lambda x,y: x+y, [1,2,3,4,5])

    '''
    [1,2,3,4,5]
    [(1,2),3,4,5]
    [(3),3,4,5] --> [(3,3),4,5]
    [(6),4,5] ---> [(6,4),5]
    [(10),5] --> [(10,5)]
    [15]
    '''

    p = map(lambda x: x*2, [1,2,3,4,5])

    print(list(filter(lambda x: x , list(range(1,11)))))

    print ("hey..")

    def mul(a):
        r = 1
        # for i in a:
        #     r = r * i
        return (r)


    showingToMari = list(map(mul, [1,2,3,4,5]))
    print(showingToMari)

    ----------------------------------------------------------------------
EXAMPLE 1: MAPPING AND LAMBDA

def mul(x):
    return (x*x)

def add(x):
    return (x+x)


func=[mul,add]
for i in range(5):
    value=map(lambda x:x(i),func)
    print(value)  


EXAMPLE 2: FILTER

number_list = range(-5, 5)
less_than_zero = list(filter(lambda x: x < 0, number_list))
print(less_than_zero)


EXAMPLE 3: LAMBDA

a=[1,2,3,50]
b=[8,9,8,7]
c=[5,52,7,1]

print(map(lambda x,y,z:x+y+z, a,b,c))
