arr=list(map(int,input().split()))
even_pos=[]
odd_pos=[]
for i in range(len(arr)):
    if i%2==0:
        even_pos.append(arr[i])
    else:
        odd_pos.append(arr[i])
even_pos.sort()
odd_pos.sort()
print(even_pos[-2]+odd_pos[-2])