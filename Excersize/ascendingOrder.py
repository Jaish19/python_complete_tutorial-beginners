def BubbleSort(set_of_list):
    
    for check in range(len(set_of_list)-1,0,-1): # 9-1=8
        for i in range(check):
        
            if set_of_list[i]>set_of_list[i+1]:
                temp=set_of_list[i]
                set_of_list[i]=set_of_list[i+1]
                set_of_list[i+1]=temp
                

set_of_list = [54,26,93,17,77,31,4,55,20]
BubbleSort(set_of_list)
print(set_of_list)