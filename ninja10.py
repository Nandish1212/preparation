n=int(input())
arr1=list(map(int,input().split()))
even_arr=[]
odd_arr=[]
for i in range(len(arr1)):
    if i%2==0:
        even_arr.append(arr1[i])
    else:
        odd_arr.append(arr1[i])
even_arr.sort()
odd_arr.sort()
print(even_arr)
print(odd_arr)