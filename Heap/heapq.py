import heapq

grades=[25,45,85,777,85,2,5]

print(heapq.nlargest(3,grades))
print(heapq.nsmallest(3,grades))

stock=[
    {'product':'TATA', 'price':25},
    {'product':'mahindra', 'price':525},
    {'product':'Godrej', 'price':255},
    {'product':'voltas', 'price':325}
    ]

print(heapq.nlargest(2,stock, key=lambda stock: stock['price']))
