__author__ = 'Sanjay'


# http://interactivepython.org/runestone/static/pythonds/SortSearch/TheBinarySearch.html
# It is possible to take greater advantage of the ordered list if we are clever with our comparisons. 
# In the sequential search, when we compare against the first item, there are at most n−1n−1 more items to look through 
# if the first item is not what we are looking for. Instead of searching the list in sequence, a binary search will start
# by examining the middle item. If that item is the one we are searching for, we are done.
#  If it is not the correct item, we can use the ordered nature of the list to eliminate half of the remaining items.
#   If the item we are searching for is greater than the middle item, we know that the entire lower half 
#   of the list as well as the middle item can be eliminated from further consideration.
#  The item, if it is in the list, must be in the upper half.

def binarySearch(alist, item):
    first = 0
    last = len(alist)-1
    found = False

    while first<=last and not found:
        midpoint = (first + last)//2
        if alist[midpoint] == item:
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1

    return found


#2nd - Recursive binary search Method
def binarySearch2(alist, item):
    if len(alist) == 0:
        return False
    else:
        midpoint = len(alist)//2
        if alist[midpoint]==item:
          return True
        else:
            if item<alist[midpoint]:
                return binarySearch(alist[:midpoint],item)
            else:
                return binarySearch(alist[midpoint+1:],item)



if __name__ == '__main__':
    testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
    print(binarySearch(testlist, 3))
    print(binarySearch(testlist, 13))
