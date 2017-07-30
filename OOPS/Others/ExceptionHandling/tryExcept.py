# Author = __Sanjay

from __future__ import division
def isDivide(x,y):
    try:
        if x >= 1:
            if x > y:
                print abs(x/y)
            elif y > x:
                print abs(y/x)
            else:
                raise ZeroDivisionError
    except ZeroDivisionError as e:
        print (e.message)
    else:
        print ("inside else")
    finally:
        print ("inside finally")
        # raise ZeroDivisionError

if __name__ == '__main__':
    isDivide(1, 10)
    # isDivide(10, 0)



#METHOD 2
import sys

randomList = ['a', 0, 2]

for entry in randomList:
    try:
        print("The entry is", entry)
        r = 1/int(entry)
        break
    except:
        print("Oops!",sys.exc_info()[0],"occured.")
        print("Next entry.")
        print()
print("The reciprocal of",entry,"is",r)


# METHOD 3


