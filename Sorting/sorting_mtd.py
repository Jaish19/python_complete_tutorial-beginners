Sorting Methods:
1.

jai=[12,3,5,8,5]
print(sorted(jai))

2.

jai=[12,3,5,8,5]
jai.sort()
print(jai)

3.

print(sorted({1: 'D', 2: 'B', 3: 'B', 4: 'E', 5: 'A'}))

4.

student_tuples = [
     ('john', 'A', 15),
     ('jane', 'B', 12),
     ('dave', 'B', 10),
 ]
print(sorted(student_tuples, key=lambda cans: cans[2]))   # sort by age

To understand:

jai=[(25,1),(85,5),(98,3),(77,2)]
print(sorted(jai,key=lambda niss:niss[0])


5.

sorted("This is a test string from Andrew".split(), key=str.lower)
['a', 'Andrew', 'from', 'is', 'string', 'test', 'This']


6.

class Student:
     def __init__(self, name, grade, age):
         self.name = name
         self.grade = grade
         self.age = age
     def __repr__(self):
         return repr((self.name, self.grade, self.age))
      
student_objects = [
     Student('john', 'A', 15),
     Student('jane', 'B', 12),
     Student('dave', 'B', 10),
 ]
print(sorted(student_objects, key=lambda jai: jai.age))


7.

from operator import itemgetter
student_tuples = [
     ('john', 'A', 15),
     ('jane', 'B', 12),
     ('dave', 'B', 10),
 ]
print(sorted(student_tuples, key=itemgetter(2)))


# 8. Example for itemgetter and attrgetter


from operator import itemgetter
class Student:
     def __init__(self, name, grade, age):
         self.name = name
         self.grade = grade
         self.age = age
     def __repr__(self):
         return repr((self.name, self.grade, self.age))
      
student_objects = [
     Student('john', 'A', 15),
     Student('jane', 'B', 12),
     Student('dave', 'B', 10),
 ]
print(sorted(student_objects, key=attrgetter('age')))

# 9. Example for itemgetter and attrgetter

from operator import itemgetter, attrgetter

class Student:
     def __init__(self, name, grade, age):
         self.name = name
         self.grade = grade
         self.age = age
     def __repr__(self):
         return repr((self.name, self.grade, self.age))
      
student_objects = [
     Student('john', 'A', 15),
     Student('jane', 'B', 12),
     Student('dave', 'C', 10),
 ]
print(sorted(student_objects, key=attrgetter('age')))

# 10.The operator module functions allow multiple levels of sorting. For example, to sort by grade then by age:

from operator import itemgetter
student_tuples = [
     ('john', 'A', 15),
     ('jane', 'B', 12),
     ('dave', 'B', 10),
 ]
print(sorted(student_tuples, key=itemgetter(1,2)))

# 11.The operator module functions allow multiple levels of sorting. For example, to sort by grade then by age:

from operator import itemgetter, attrgetter

class Student:
     def __init__(self, name, grade, age):
         self.name = name
         self.grade = grade
         self.age = age
     def __repr__(self):
         return repr((self.name, self.grade, self.age))
      
student_objects = [
     Student('john', 'A', 15),
     Student('jane', 'B', 12),
     Student('dave', 'C', 10),
 ]
print(sorted(student_objects, key=attrgetter('grade','age')))

# 12.ASCENDING AND DECENDING ORDER

from operator import itemgetter
student_tuples = [
     ('john', 'A', 15),
     ('jane', 'B', 12),
     ('dave', 'B', 10),
 ]
print(sorted(student_tuples, key=itemgetter(2), reverse=True))

# 13.ASCENDING AND DECENDING ORDER


from operator import itemgetter, attrgetter

class Student:
     def __init__(self, name, grade, age):
         self.name = name
         self.grade = grade
         self.age = age
     def __repr__(self):
         return repr((self.name, self.grade, self.age))
      
student_objects = [
     Student('john', 'A', 15),
     Student('jane', 'B', 12),
     Student('dave', 'C', 10),
 ]
print(sorted(student_objects, key=attrgetter('age'),reverse=True))


# 14. Sort Stability and Complex Sorts

data = [('red', 1), ('blue', 1), ('red', 2), ('blue', 2)]
print(sorted(data, key=itemgetter(0)))

# 15. Sort Stability and Complex Sorts

from operator import itemgetter, attrgetter

class Student:
     def __init__(self, name, grade, age):
         self.name = name
         self.grade = grade
         self.age = age
     def __repr__(self):
         return repr((self.name, self.grade, self.age))
      
student_objects = [
     Student('john', 'A', 15),
     Student('jane', 'B', 12),
     Student('dave', 'B', 10),
 ]
s=sorted(student_objects, key=attrgetter('age'))
print(sorted(s,key=attrgetter('grade'),reverse=True))

