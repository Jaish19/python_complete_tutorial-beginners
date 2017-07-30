# COUNTER 

# INPUT

# aaaaabbbbbccc

# OUTPUT
# aaaaabbbbbccc
# Counter({'a': 5, 'b': 5, 'c': 3})
# ('a', 5)
# ('c', 3)
# ('b', 5)



from collections import Counter
val=str(raw_input())
   
print(val)

counts=Counter(val)
print(counts)
for k,v in counts.items():
    print(k,v)
   
   
   
   
   