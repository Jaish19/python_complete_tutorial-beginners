from operator import attrgetter
import heapq
class person:
    def __init__(self,name,ID,subjects,marks):
        self.name=name
        self.ID=ID
        self.subjects=subjects
        self.marks=marks
        
    def DataLogging(self, log):
        dataBase=[]
        notaBase=[]
        for i in range(len(self.subjects)):
            nurture=(self.subjects[i] + "=" + self.marks[i])
            mature=(log.subjects[i] + "=" + log.marks[i])
            dataBase.append(nurture)
            notaBase.append(mature)
            
        print(dataBase)
        print(notaBase)
#         print(heapq.nlargest(2,dataBase))
        
        for i in range(len(self.marks)):
            if self.marks[i]>log.marks[i]:
                print(self.name,"is highest score in",self.subjects[i],"and the mark is",self.marks[i])
            else:
                print(log.name,"is highest score in", log.subjects[i],"and the mark is",log.marks[i])
            
        
        
        
        
        


p1=person("jai","AUB1011",["maths","science","tamil"],['96','93','94'])
p2=person("vijay","AUB1021",["maths","science","tamil"],["96","92","84"])
p1.DataLogging(p2)