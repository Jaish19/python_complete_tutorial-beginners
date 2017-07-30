__author__ = 'Sanjay Pradeep'


def findPrime():

    # num = int(input("Enter a number: "))
    #
    # # prime numbers are greater than 1
    # if num > 1:
    #    # check for factors
    #    for i in range(2,num):
    #        if (num % i) == 0:
    #            print(num,"is not a prime number")
    #            print(i,"times",num//i,"is",num)
    #            break
    #    else:
    #        print(num,"is a prime number")
    #
    # # if input number is less than
    # # or equal to 1, it is not prime
    # else:
    #    print(num,"is not a prime number")
    # s= []
    # for i in args:
    #     print i
    #     if i >1:
    #         for j in range(2,i):
    #             if (i%j) == 0:
    #                 break
    #         else:
    #             s.append(i)
    #     else:
    #         break
    l = [5,3,11,16,17]
    s= []
    for i in l:
        if i > 1:
            for j in range(2,i):
                if (i % j) == 0:
                    break
                else:
                    s.append(i)
            else:
                break
    print (s)


if __name__ == '__main__':
    # l = [5,3,11,16,17]
    # findPrime(l)
    findPrime()





#PRIME NUMBER
    def prime(val):
    count=0
    if val>1:
        for i in range(2, val):
            if val % i == 0:
                count=count+1

        if(count==0):
            print("its prime number")
        else:
            print("its not prime number")
        
           
                
    else:
        print("please enter greater than 1")
        
        
prime(63)



# __author__ = 'Sanjay Pradeep'
# PRIME NUMBER FROM LIST

def prime(val):
    for i in val:
        
        print(i)
        if(i>1):
            count=0
            for j in range(2,i):
                if i%j == 0:
                    count=count+1
            if(count==0):
                print("Its prime number")
            else:
                print("Its not a prime number")
               
            
l1=[1,2,3,4,5]                
prime(l1)