__author__ = 'Sanjay'
#
# Task
#
# You are the manager of a supermarket.
#  You have a list of N
# N
#  items together with their prices that consumers bought on a particular day.
#  Your task is to print each item_name and net_price in order of its first occurrence.
#
# item_name = Name of the item.
# net_price = Quantity of the item sold multiplied by the price of each item.
#
#
# Input Format
#
#
# The first line contains the number of items, N
# N
# .
#  The next N
# N
#  lines contains the item's name and price, separated by a space.
#
# Constraints
#
# 0<N?100
# 0<N?100
#
#
# Output Format
#
#
# Print the item_name and net_price in order of its first occurrence.
#
#
# Sample Input
#
# 9
# BANANA FRIES 12
# POTATO CHIPS 30
# APPLE JUICE 10
# CANDY 5
# APPLE JUICE 10
# CANDY 5
# CANDY 5
# CANDY 5
# POTATO CHIPS 30
#
#
#
# Sample Output
#
# BANANA FRIES 12
# POTATO CHIPS 60
# APPLE JUICE 20
# CANDY 20
#
#
#
# Explanation
#
#
# BANANA FRIES: Quantity bought: 1
# 1
# , Price: 12
# 12
#
# Net Price: 12
# 12
#
# POTATO CHIPS: Quantity bought: 2
# 2
# , Price: 30
# 30
#
# Net Price: 60
# 60
#
# APPLE JUICE: Quantity bought: 2
# 2
# , Price: 10
# 10
#
# Net Price: 20
# 20
#
# CANDY: Quantity bought: 4
# 4
# , Price: 5
# 5
#
# Net Price: 20
# 20
from collections import OrderedDict
d=OrderedDict()
for _ in range(int(raw_input())):
    item, quantity = raw_input().split(' ')
    d[item] = int(quantity)
    
print(d)
for item, quantity in d.items():
    print(item, quantity)



  # EXAMPLE CODE FOR DICTIONARY AND ORDERED_DICT:

  # An OrderedDict is a dictionary subclass that remembers the order in which its contents are added.

  import collections

print 'Regular dictionary:'
d = {}
d['a'] = 'A'
d['b'] = 'B'
d['c'] = 'C'
d['d'] = 'D'
d['e'] = 'E'

for k, v in d.items():
    print k, v

print '\nOrderedDict:'
d = collections.OrderedDict()
d['a'] = 'A'
d['b'] = 'B'
d['c'] = 'C'
d['d'] = 'D'
d['e'] = 'E'

for k, v in d.items():
    print k, v



 # A regular dict does not track the insertion order, and iterating over it produces the values 
 # in an arbitrary order. In an OrderedDict, by contrast, the order the items are inserted is remembered 
 # and used when creating an iterator.

 # OUTPUT:



Regular dictionary:
a A
c C
b B
e E
d D

OrderedDict:
a A
b B
c C
d D
e E

EXAMPLE 2 FOR ORDERED_DICT:

A regular dict looks at its contents when testing for equality. An OrderedDict also considers the 
order the items were added.



import collections

print 'dict       :',
d1 = {}
d1['a'] = 'A'
d1['b'] = 'B'
d1['c'] = 'C'
d1['d'] = 'D'
d1['e'] = 'E'

d2 = {}
d2['e'] = 'E'
d2['d'] = 'D'
d2['c'] = 'C'
d2['b'] = 'B'
d2['a'] = 'A'

print d1 == d2

print 'OrderedDict:',

d1 = collections.OrderedDict()
d1['a'] = 'A'
d1['b'] = 'B'
d1['c'] = 'C'
d1['d'] = 'D'
d1['e'] = 'E'

d2 = collections.OrderedDict()
d2['e'] = 'E'
d2['d'] = 'D'
d2['c'] = 'C'
d2['b'] = 'B'
d2['a'] = 'A'

print d1 == d2

OUTPUT:

dict       : True
OrderedDict: False