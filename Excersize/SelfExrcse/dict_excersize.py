# http://www.w3resource.com/python-exercises/dictionary/

# 1. Write a Python script to sort (ascending and descending) a dictionary by value. Go to the editor

# WITH OPERATOR

import operator
dict_set={'jai':2,'vijay':3,'suresh':47,'saraswathi':99,'raji':85}
sort_one=sorted(dict_set.items(), key=operator.itemgetter(1))
print("Ascending values are:",sort_one)
sort_two=sorted(dict_set.items(), key=operator.itemgetter(1),reverse=True)
print("Decending values are:",sort_two)

#WITHOUT OPERATOR

dict_set={'jai':2,'vijay':3,'suresh':47,'saraswathi':99,'raji':85}
sort_one=sorted(dict_set.items(), key=lambda(k,v),(v,k))
print("Ascending values are:",sort_one)
sort_two=sorted(dict_set.items(), key=lambda(k,v),(-v,k))
print("Decending values are:",sort_two)


---------------------------------------------------------------------------------------

# . Write a Python script to add a key to a dictionary. Go to the editor

# Sample Dictionary : {0: 10, 1: 20}
# Expected Result : {0: 10, 1: 20, 2: 30}

M-1:

dict_set={'jai':2,'vijay':3,'suresh':47,'saraswathi':99,'raji':85}
sep=['ganesh','jaish']
for i in sep:
    dict_set[i]=len(i)
    
print(dict_set)

-----------------------------------------------------------------------------

M-2:

dict_set={'jai':2,'vijay':3,'suresh':47,'saraswathi':99,'raji':85}
sep=['ganesh','jaish']
dict_set.update({"ganesh":54})

print(dict_set)

---------------------------------------

===================================================================================

# 3. Write a Python script to concatenate following dictionaries to create a new one. Go to the editor

# Sample Dictionary : 
# dic1={1:10, 2:20} 
# dic2={3:30, 4:40} 
# dic3={5:50,6:60}
# Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}


dic1={1:10, 2:20} 
dic2={3:30, 4:40} 
dic3={5:50,6:60}
dic4={}
for i in (dic1,dic2,dic3):
    dic4.update(i)

print(dic4)
=====================================================================================================

# 4. Write a Python script to check if a given key already exists in a dictionary.

def check_dict(x):
    

    dic1={1:10, 2:20} 
    dic2={3:30, 4:40} 
    dic3={5:50,6:60}
    dic4={}
    for i in (dic1,dic2,dic3):
        dic4.update(i)
        
    if x in dic4:
        print("its available")
    else:
        print("its not available")
        
        
check_dict(5)


# 5. iterate the key and values using for

dict={1:10, 2:20,3:30, 4:40,5:50,6:60}
for k,v in dict.iteritems():
    print(k,v)

# 6.Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x). Go to the editor
# Sample Dictionary ( n = 5) : 
# Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

c={x:x*x for x in range(5)}
print(c)



# 7. Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are square of keys. Go to the editor
# Sample Dictionary 
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}

c={x:x*x for x in range(15)}
print(c)



# 10. Write a Python program to sum all the items in a dictionary. Go to the editor
# Click me to see the sample solution

print(sum(dict.values()))


# 11. Write a Python program to multiply all the items in a dictionary. Go to the editor
# Click me to see the sample solution

c=''    
# print(sum(dict.values()))
for k,v in dict.items():
	# c=c*v or
    c=c*dict[k] 
print(c)


# 12. Write a Python program to remove a key from a dictionary. Go to the editor
# Click me to see the sample solution

METHOD 1:

dict={1:10, 2:20,3:30, 4:40,5:50,6:60}
for k,v in dict.items():
    del dict[k]
     
print(dict)

METHOD 2:

if 1 in dict:
    del dict[1]
    
print(dict)

# 13. Write a Python program to map two lists into a dictionary. Go to the editor
# Click me to see the sample solution

l1=[1,2,3,4]
l2=[4,5,6,7]
print(dict(zip(l1,l2)))

# 14. Write a Python program to sort a dictionary by key. Go to the editor
# Click me to see the sample solution

import operator
l1=[1,2,3,4]
l2=[4,5,6,7]
l3=dict(zip(l1,l2))
one={5:3,8:2,3:1,2:9}
# Technique 1:
sorted_one= sorted(one.iteritems(), key=operator.itemgetter(0),reverse=True)
# Technique 2:
print(sorted(one.iteritems(),key=lambda (k,v): (v,k)))
print(sorted_one)


# 15. Write a Python program to get the maximum and minimum value in a dictionary. Go to the editor
# Click me to see the sample solution

BEST AND EASY MTD:

dict={1:1000,5:411,8:987,6:214}
max_val=max(dict.keys()) 
min_val=min(dict.keys())
# output: (8, 1)
max_val=max(dict.values())
min_val=min(dict.values())
#output: (1000, 214)


METHOD 2:

dict={1:1000,5:411,8:987,6:214}

key_max = max(my_dict.values(), key=(lambda v: v))
key_min = min(my_dict.values(), key=(lambda v: v))

print(key_max,key_min)
print(dict[key_max],dict[key_min])

key_max = max(my_dict.keys(), key=(lambda k: k))
key_min = min(my_dict.keys(), key=(lambda k: k))

----------------------------------------------------------------------------

# 16.Write a Python program to get a dictionary from an object's fields. Go to the editor
# Click me to see the sample solution

class dict(object):
    def __init__(self):
        self.x='jai'
        self.y='success'
        
test=dict()
print(test.__dict__)

--------------------------------------------------------------
# 17. Write a Python program to remove duplicates from Dictionary. Go to the editor
# Click me to see the sample solution


student_data = {'id1': 
   {'name': ['Sara'], 
    'class': ['V'], 
    'subject_integration': ['english, math, science']
   },
 'id2': 
  {'name': ['David'], 
    'class': ['V'], 
    'subject_integration': ['english, math, science']
   },
 'id3': 
    {'name': ['Sara'], 
    'class': ['V'], 
    'subject_integration': ['english, math, science']
   },
 'id4': 
   {'name': ['Surya'], 
    'class': ['V'], 
    'subject_integration': ['english, math, science']
   },
}

result = {}

for key,value in student_data.items():
    if value not in result.values():
        result[key] = value

print(result)

-------------------------------------------------------------------------------------
# 18.Write a Python program to check a dictionary is empty or not.



my_dict = {}

if len(my_dict)==0:
    print("dict empty")
if not bool(my_dict):
    print("Dictionary is empty")


----------------------------------------------------------------------------------------------
# 19. Write a Python program to combine two dictionary adding values for common keys.

BEST METHOD:

from collections import Counter
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
d3={}

d = Counter(d1) + Counter(d2)
d3.update(d)
print(d3)

ALTERNATIVE METHOD:

d1 = {'a': 100, 'b': 200,'c':800}
d2 = {'b': 300, 'a': 200,'d':900}
d3={}

for k,v in d1.items():
    
    if k in d2:
        d3[k]=d1[k]+d2[k] 
    else:
        d3[k]=v
        
print(d3)
    
        
-----------------------------------------------------------------------------------------------------

# 20. Write a Python program to print all unique values in a dictionary. Go to the editor
# Sample Data : [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
# Expected Output : Unique Values: {'S005', 'S002', 'S007', 'S001', 'S009'}

BEST METHOD:

dict=[{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
store=set(val for n in dict for val in n.values())
print(store)


method 2:

dict=[{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
s1=[]
for dic in dict:
    for val in dic.values():
         
        s1.append(val)
         
print(set(s1))

-------------------------------------------------------------------------

# 21. Write a Python program to create and display all combinations of letters, selecting each letter from a different key in a dictionary. Go to the editor
# Sample data : {'1':['a','b'], '2':['c','d']}
# Expected Output: 
# ac
# ad
# bc
# bd
BEST METHOD:

import itertools      
d ={'1':['a','b'], '2':['c','d']}
for combo in itertools.product(*[d[k] for k in sorted(d.keys())]):
    print(''.join(combo))


METHOD 1:

from itertools import product
dict={'1':['a','b'], '2':['c','d']}
c=[]
for values in dict.values(
    c.append(values)


c=product(c[0],c[1])

for i in c:
    print("".join(i))


-------------------------------------------------------------------------------

# 22. Write a Python program to find the highest 3 values in a dictionary. Go to the editor
# Click me to see the sample solution

from heapq import nlargest

dict={'Jai': 800,'Shalini':900,'Suresh':580,'Saraswathi':1500,'Vijay':850}
three_largest=nlargest(3,dict,key=dict.get)
print(three_largest)


--------------------------------------------------------------------------------------

# 23. Write a Python program to combine values in python list of dictionaries. Go to the editor
# Sample data: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
# Expected Output: Counter({'item1': 1150, 'item2': 300})
# Click me to see the sample solution


from collections import Counter
item_list = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]

result = Counter()

for d in item_list:
    result[d['item']] += d['amount']
print(result) 

----------------------------------------------------------------------------------------

# 24. Write a Python program to create a dictionary from a string. Go to the editor
# Note: Track the count of the letters from the string.
# Sample string : 'w3resource'
# Expected output: {'3': 1, 's': 1, 'r': 2, 'u': 1, 'w': 1, 'c': 1, 'e': 2, 'o': 1}
# Click me to see the sample solution

from collections import Counter
jai='w3jaishalini'
print(Counter(jai))

------------------------------------------------------------------------------------------

# 25. Write a Python program to print a dictionary in table format. Go to the editor
# Click me to see the sample solution


Need to observe lott.....
---------------------------------------------------------------------------------------
# 26. Write a Python program to count the values associated with key in a dictionary. Go to the editor
# Sample data: = [{'id': 1, 'success': True, 'name': 'Lary'}, {'id': 2, 'success': False, 'name': 'Rabi'}, {'id': 3, 'success': True, 'name': 'Alex'}]
# Expected result: Count of how many dictionaries have success as True
# Click me to see the sample solution


student = [{'id': 1, 'success': True, 'name': 'Lary'},
 {'id': 2, 'success': False, 'name': 'Rabi'},
 {'id': 3, 'success': True, 'name': 'Alex'}]
print(sum(d['success'] for d in student))

-------------------------------------------------------------------------------------------------

# 27. Write a Python program to convert a list into a nested dictionary of keys. Go to the editor
# Click me to see the sample solution

num_list = [1, 2, 3, 4]
new_dict = Current = {}
for name in num_list:
    current[name] = {}
    current = current[name]

print(new_dict)

--------------------------------------------------------------------------------------------------

# 28. Write a Python program to sort a list alphabetically in a dictionary. Go to the editor
# Click me to see the sample solution

num = {'n1': [2, 3, 1], 'n2': [5, 1, 2], 'n3': [3, 2, 4]}

sorted_ans={key: sorted(value) for key,value in num.items()}
print(sorted_ans)


----------------------------------------------------------------------------------------------------

# 29. Write a Python program to remove spaces from dictionary keys. Go to the editor
# Click me to see the sample solution.

from heapq import nlargest
from operator import itemgetter
data= {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
three_large=nlargest(3,data.items(), key=itemgetter(1))
print(three_large)

----------------------------------------------------------------------------------------------------
# 31. Write a Python program to get the key, value and item in a dictionary. Go to the editor
# Click me to see the sample solution

dict_num = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60, 6:80}
print("      key  value  count")
for count, (key, value) in enumerate(dict_num.items(),1):
    print(key,'   ',value,'    ', count)

------------------------------------------------------------------------------------------------------

# 32. Write a Python program to print a dictionary line by line. Go to the editor
# Click me to see the sample solution

students = {'Aex':{'class':'V',
        'rolld_id':2},
        'Puja':{'class':'V',
        'roll_id':3}}
for a in students:
    print(a)
    for b in students[a]:
        print (b,':',students[a][b])

------------------------------------------------------------------------------------------------

# 33. Write a Python program to check multiple keys exists in a dictionary. Go to the editor
# Click me to see the sample solution

student = {
  'name': 'Alex',
  'class': 'V',
  'roll_id': '2'
}
print(student.keys() >= {'class', 'name'})
print(student.keys() >= {'name', 'Alex'})
print(student.keys() >= {'roll_id', 'name'})

--------------------------------------------------------------------------------------
# 34. Write a Python program to count number of items in a dictionary value that is a list. Go to the editor
# Click me to see the sample solution

dict =  {'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']}
s=0
for v in dict.values():
    s=s+len(v)
    
print("Count of values are:",s)

---------------------------------------------------------------------------

# 35. Write a Python program to sort Counter by value. Go to the editor
# Sample data : {'Math':81, 'Physics':83, 'Chemistry':87}
# Expected data: [('Chemistry', 87), ('Physics', 83), ('Math', 81)]

from collections import Counter
data = {'Math':81, 'Physics':83, 'Chemistry':87, 'Chemistry':98}
x=Counter(data)
print(x.most_common())

-------------------------------------------------------------------------

36. Write a Python program to create a dictionary from two lists without losing duplicate values. Go to the editor
Sample lists: ['Class-V', 'Class-VI', 'Class-VII', 'Class-VIII'], [1, 2, 2, 3]
Expected Output: defaultdict(<class 'set'>, {'Class-VII': {2}, 'Class-VI': {2}, 'Class-VIII': {3}, 'Class-V': {1}})
Click me to see the sample solution

METHOD 1:

lists= ['Class-V', 'Class-VI', 'Class-VII', 'Class-VIII']
list_two=[1,2,3,4]
c=zip(lists,list_two)
print(dict(c))

METHOD 2:

from collections import defaultdict
class_list = ['Class-V', 'Class-VI', 'Class-VII', 'Class-VIII']
id_list = [1, 2, 2, 3]
temp = defaultdict(set)
for c, i in zip(class_list, id_list):
    print(c,i)
    temp[c].add(i)
print(temp)

-----------------------------------------------------------------------------------
# 37. Write a Python program to replace dictionary values with their sum. Go to the editor
# Click me to see the sample solution

def bank_statements(*args):
    for d in args:
        n1=d.pop('Current Balance')
        n2=d.pop('Fixed Account')
        d['Overall_Account']=n1+n2
        yield d
    

n=(bank_statements({"Name":'Suresh', 'Age': 50, 'Current Balance':200, "Fixed Account":9000}, {"Name":'Saraswathi', 'Age': 45, 'Current Balance':100, "Fixed Account":5000}))

for i in n:
    print(i)


----------------------------------------------------------------------------------

# 38. Write a Python program to convert a dictionary to OrderedDict. Go to the editor
# Click me to see the sample solution

import collections
student = [("Student_name", "Alex"),
        ("ID", 5),
        ("Class", 'V'),
        ("Country", 'USA')]

student = collections.OrderedDict(student)
print(student)

---------------------------------------------------------------------------------
# 39. Write a Python program to match key values in two dictionaries. Go to the editor
# Sample dictionary: {'key1': 1, 'key2': 3, 'key3': 2}, {'key1': 1, 'key2': 2}
# Expected output: key1: 1 is present in both x and y
# Click me to see the sample solution

x = {'key1': 1, 'key2': 3, 'key3': 2,}
y = {'key1': 1, 'key2': 2}

for (key, value) in set(x.items()) & set(y.items()):
    print('%s: %s is present in both x and y' % (key, value))

----------------------------------------------------------------------------------