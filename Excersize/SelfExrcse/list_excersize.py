# IMPORTANT LINK: http://www.w3resource.com/python-exercises/list/
=============================================================================

# 1. Write a Python program to sum all the items in a list. Go to the editor
# Click me to see the sample solution

l1=[1,2,3,4,5,6]
print(reduce(lambda x,y:x+y,l1))
----------------
print(sum(l1))

----------------

def sum(alist):
    s=0
    for i in alist:
        s+=i
        
    print(s)
    
sum([1,2,3,4,5])

==============================================================================
# 2. Write a Python program to multiplies all the items in a list. Go to the editor
# Click me to see the sample solution

def mul(alist):
    s=1
    for i in alist:
        s*=i
        
    print(s)
    
sum([1,2,3,4,5])

------------------------------------
l1=[1,2,3,4,5]
print(reduce(lambda x,y:x*y,l1))

===================================================
# 3. maximum value from the list

l1=[1,2,3,4,5]
print(max(l1))

==================================
# 4.Smallest number from the list

l1=[1,2,3,4,5]
print(min(l1))
===========================
# 6. Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples. Go to the editor 
# Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
# Click me to see the sample solution

from operator import itemgetter
l1=[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
print(sorted(l1,key=itemgetter(1)))

=============================================
# 5. Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings. Go to the editor 
# Sample List : ['abc', 'xyz', 'aba', '1221']
# Expected Result : 2
# Click me to see the sample solution

def task(words):
    ctr=0
    for word in words:
        if len(word)>1 and word[0] == word[-1]:
            ctr+=1
    return ctr


print(task(['abc', 'xyz', 'aba','yxy','1221']))

===================================================
# 7. Write a Python program to remove duplicates from a list. Go to the editor
# Click me to see the sample solution

l1=[1,1,1,2,5,5,8,5,5]
print(set(l1))

-----------------------


l1=[1,1,1,2,5,5,8,5,5,8,9,9,7,8,8]
l2=[]
for i in l1:
    if i not in l2:
        l2.append(i)
    else:
        pass
    
print(l2)	

=========================================

# 8. Write a Python program to check a list is empty or not. Go to the editor
# Click me to see the sample solution

l1=[1,1,1,2,5,5,8,5,5,8,9,9,7,8,8]
l2=[]
print(len(l2))  
---------------------------------------

l2=[]
if not l2:
    print("list is empty")
else:
    print("There's content")

===========================================
# 9. Write a Python program to clone or copy a list. Go to the editor
# Click me to see the sample solution

l2=[1,2,3,4,5]
l3=l2
print(l3)

-------------------

l2=[1,2,3,4,5]
l3=list(l2)
print(l3)	

=================================================

# 10. Write a Python program to find the list of words that are longer than n from a given list of words. Go to the editor
# Click me to see the sample solution

def find(n, words):
    word=words.split()
    l1=[]
    [l1.append(i) for i in word if len(i)>2] 
    return l1

print(find(3,"Hi everyone this is very important issue to be announce"))

=========================================================
# 11. Write a Python function that takes two lists and returns True if they have at least one common member. Go to the editor
# Click me to see the sample solution

def func(l1,l2):
    if len(l1)==len(l2):
        for i in l1:
            if i in l2:
                print("The contents are repeating")
                break
            else:
                pass
            
l1=[1,2,3,4]
l2=[4,5,6,7]
func(l1,l2)

=========================================================
# 12. Write a Python program to print a specified list after removing the 0th, 4th and 5th elements. Go to the editor
# Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# Expected Output : ['Green', 'White', 'Black']
# Click me to see the sample solution

l1=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
l3=[]
for x,y in enumerate(l1):
    if x not in (0,4,5):
        l3.append(y)
        
print(l3)


=============================================================
# 13. Write a Python program to generate a 3*4*6 3D array whose each element is *.

array=[[['*' for row in range(3)]for col in range(5)]for col in range(6)]
print(array)
===========================================
# 14. Write a Python program to print the numbers of a specified list after removing even numbers from it. Go to the editor
# Click me to see the sample solution

l1=[i for i in range(10) if i%2==1]
print(l1)

===================================
# Write a Python program to shuffle and print a specified list.


from random import shuffle
l1=['red','blue','brown','orange']
shuffle(l1)
print(l1)

================================================
# 16. Write a Python program to generate and print a list of first and last 5 elements where the values are square of numbers between 1 and 30 (both included). Go to the editor
# Click me to see the sample solution

def operation(n,val):
    l1=[]
    for i in n:
        if i in val:
            l1.append(i**2)
        else:
            l1.append(i)
            
    return l1

print(operation(range(1,31),[1,2,3,4,5,26,27,28,29,30]))

----------------------------


def printValues():
    l = list()
    for i in range(1,21):
        l.append(i**2)
    print(l[:5])
    print(l[-5:])

printValues()

=======================================================
# 17. Write a Python program to generate and print a list except for the first 5 elements, 
# where the values are square of numbers between 1 and 30 (both included).
def printValues():
	l = list()
	for i in range(1,21):
		l.append(i**2)
	print(l[5:])

printValues()

=========================================
# 18. create perumutations

import itertools
print(list(itertools.permutations([1,2,3])))
==============================

# 19. Write a Python program to get the difference between the two lists. Go to the editor
# Click me to see the sample solution

l1=set([1,2,3,4,5])
l2=set([1,2,3,8,9])

print(l1.difference(l2))
------------------
l1=set([1,2,3,4,5])
l2=set([1,2,3,8,9])

print(list(l1-l2))

======================================================
# 20. Write a Python program access the index of a list. Go to the editor
# Click me to see the sample solution
l1=[1,2,3,4,5]
for i,j in enumerate(l1):
    print(i,j)
==========================================================

# 21. Write a Python program to convert a list of characters into a string. Go to the editor
# Click me to see the sample solution

l1=raw_input("Enter the value").split()
print(''.join(l1))

=======================================

# 22. Write a Python program to find the index of an item in a specified list. Go to the editor
# Click me to see the sample solution

L1=[1,2,3]
print(l1.index(3))

===============================
# Write a Python program to flatten a shallow list.

import itertools
l1=[[1,2,3],[4,5,6],[9],[8,5,6]]
new_list=list(itertools.chain(*l1))
print(new_list)
===========================================
# Write a Python program to append a list to the second list.

list1 = [1, 2, 3, 0]
list2 = ['Red', 'Green', 'Black']
final_list = list1 + list2
print(final_list)

-------------------------

list1.append(list2)
---------------------------------------

# 25. Write a Python program to select an item randomly from a list. Go to the editor
# Click me to see the sample solution
import random
l1=[1,2,3,4,5]
print(random.choice(l1))

==========================================
# Write a Python program to find the second smallest number in a list.

l1=[1,2,3,4,5,-1]

l1.remove(min(l1))
print(min(l1))

=====================================
# Write a Python program to find the second largest number in a list.

l1=[1,2,3,4,5,-1]

l1.remove(max(l1))
print(max(l1))

=============================================
# 31. Write a Python program to count the number of elements in a list within a specified range. Go to the editor
# Click me to see the sample solution

def counts_check(l1,min_val,max_val):
    ctr=0
    for i in l1:
        if min_val <= i <= max_val:
            ctr+=1
    return ctr


l1=[1,2,3,4,5,6,7,8,9]
print(counts_check(l1,3,9))

l1=['a','b','c','d','e','f']
print(counts_check(l1,'b','f'))

===========================================
# Write a Python program to generate all sublists of a list.


def sub_lists(l1):
    subs=[]
    for i in range(len(l1)):
        n=i+1
        while n<=len(l1):
            sub=l1[i:n]
            subs.append(sub)
            n+=1
    return subs
    
l1 = [10, 20, 30, 40]
l2 = ['X', 'Y', 'Z']
print(sub_lists(l1))
print(sub_lists(l2))
=======================================
# Write a Python program to create a list by concatenating a given list which range goes from 1 to n.

l1=['p','q']
l2=[]
for i in range(1,6):
    for j in l1:
        l2.append(j+str(i))

print(l2)

==================================================
# 37. Write a Python program to find common items from two lists. Go to the editor
# Click me to see the sample solution

l1=[1,2,3,4,5]
l2=[1,2,7,8,9]
l3=[]
try:
    for i in l1:
        if i in l2:
            l3.append(i)
        else:
            pass 
    print(l3)      
except:
    print("The error found")

======================================================================

# 39. Write a Python program to convert a list of multiple integers into a single integer. Go to the editor
# Sample list: [11, 33, 50]
# Expected Output: 113350
# Click me to see the sample solution

l1=[1,2,3,4,5,6]

l2=[]
for i in l1:
    l2.append(str(i))
    
print(''.join(l2))

============================================================
# 38. Write a Python program to change the position of every n-th value with the (n+1)th in a list. Go to the editor
# Sample list: [0,1,2,3,4,5]
# Expected Output: [1, 0, 3, 2, 5, 4]
# Click me to see the sample solution

list_op=[]

list_op=[list[i:i+2] for i in range(0,len(list),2)]
        
print(list_op)

for  i in list_op:

    nip=i[1]
    i[1]=i[0]
    i[0]=nip
    
print(list_op)

n=[]
for i in list_op:
    n.extend([i[0],i[1]]) 
    

print(n)

=============================================================================
# Write a Python program to split a list based on first character of word.

# ALTERNET METHOD:

list= [0,1,2,3,4,5]
word_list = ['be','have','do','say','get','make','go','know','take','see','come','think',
     'look','want','give','use','find','tell','ask','work','seem','feel','leave','call']

for i in sorted(word_list):
    print(i[0])
    print(i)


# BEST METHOD:

from itertools import groupby
from operator import itemgetter

word_list = ['be','have','do','say','get','make','go','know','take','see','come','think',
     'look','want','give','use','find','tell','ask','work','seem','feel','leave','call']

for letter,words in groupby(sorted(word_list),key=itemgetter(0)):
    print(letter)
    for word in words:
        print(word)

================================================================================

# Write a Python program to create multiple lists.


dict={}
for i in range(1,25):
    dict[i]=[i,i+1]
    
print(dict)

==================================================================
# 42. Write a Python program to find missing and additional values in two lists. Go to the editor
# Sample data : Missing values in second list: b,a,c
# Additional values in second list: g,h

# METHOD 1:

l1=[1,2,3,4,5,6]
l2=[1,2,3,4,7]

        
l3=[i for i in l2 if i not in l1] 
       
l4=[i for i in l1 if i not in l2]
        
        
print("Additional value in second list:",l3)
print("Missing elements in second list:",l4)

# METHOD 2:

l1=[1,2,3,4,5,6]
l2=[1,2,3,4,7]

        
l3=[i for i in l2 if i not in l1] 
       
l4=[i for i in l1 if i not in l2]
        
        
print("Additional value in second list:",','.join(set(str(l1)).difference(str(l2))))
print("Missing elements in second list:",','.join(set(str(l2)).difference(str(l1))))

===========================================================
# Write a Python program to generate groups of five consecutive numbers in a list.


l1=[[5*i + j for j in range(1,6)] for i in range(5)]
print(l1)

========================================================
Write a Python program to select the odd items of a list.


l1=[i for i in range(10) if i%2==1]
print(l1)

method 2:

l1=range(1,10)
print(l1[::2])

============================================================
# Write a Python program to convert a pair of values into a sorted unique array.

L = [(1, 2), (3, 4), (1, 2), (5, 6), (7, 8), (1, 2), (3, 4), (3, 4),
 (7, 8), (9, 10)]
print("Original List: ", L)
print("Sorted Unique Data:",sorted(set().union(*L)))

======================================================
# Write a Python program to insert an element before each element of a list.

color = ['Red', 'Green', 'Black']
print("Original List: ",color)
color = [v for elt in color for v in ('f', elt)]
print("Original List: ",color)

=========================================================
# Write a Python program to iterate over two lists simultaneously.

l1=[1,2,3,4,5]
l2=['red','blue','black']
for i,j in zip(l1,l2):
    print(i,j)

 =========================================================
# 50.Write a Python program to sort a list of nested dictionaries.

my_list = [{'key': {'subkey': 1}}, {'key': {'subkey': 10}}, {'key': {'subkey': 5}}]

print(sorted(my_list,reverse=True))

====================================================
# 51.Write a Python program to split a list every Nth element.


def check(new,values):
    print([new[i::values] for i in range(values)])
    
C = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']

check(C,3)

=======================================================
# 52. Write a Python program to compute the similarity between two lists. Go to the editor

color_one= ["red", "orange", "green", "blue", "white"] 
color_two=["black", "yellow", "green", "blue"]
print(set(color_one).difference(color_two))
print(set(color_two).difference(color_one))

=======================================================
# 56.Write a Python program to convert a string to a list.

import ast
color="['red','black']"
print(ast.literal_eval(color))

========================================================
# 53.Write a Python program to create a list with infinite elements.

import itertools
c=itertools.count()

print(next(c))
print(next(c))
print(next(c))

=======================================================
# 54.Write a Python program to concatenate elements of a list.

color = ['red', 'green', 'orange']
print('-'.join(color))
print(''.join(color))

====================================================
# 55.Write a Python program to remove key values pairs from a list of dictionaries.


# METHOD 1:

val=[{'key1': 'value1', 'key2': 'value2'}, {'key1': 'value3', 'key2': 'value4'}]                                  
new_list=[{j:k for j,k in i.items() if j!='key1' } for i in val]
print(new_list)

# METHOD 2:

val=[{'key1': 'value1', 'key2': 'value2'}, {'key1': 'value3', 'key2': 'value4'}]                                  
for i in val:
    c=i.keys()
    print(c)
    del i[c[0]]
        
        
print(val)
