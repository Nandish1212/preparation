#code15
def target_2d(arr,target):
    list1=[]
    print(len(arr))
    for i in range(len(arr)+1):
        for j in range(len(arr)+1):
           list1.append(arr[i][j]) 
    print(list1)
    if target in list1:
        return True
    else:
        return False    
arr=[[1,3,5,7],[10,11,16,20],[23,30,34,60]]    
target=7
print(target_2d(arr,target))