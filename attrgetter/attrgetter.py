from operator import attrgetter

class User:
    
    def __init__(self, x, y):
        self.name=x
        self.userId=y
        
    def __repr__(self):
        return self.name + ":" + str(self.userId)
    
    
users=[User('jai',2),
       User('vijay',34),
       User('games',33)
       ]

for user in users:
    print(user)
    
print("-----------")

for user in sorted(users, key=attrgetter('name')):
    print(user)
    
print("-----------")

for user in sorted(users, key=attrgetter('userId')):
    print(user)
    