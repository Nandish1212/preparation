n=int(input())
sum1=int(input())
arr=list(map(int,input().split()))
arr.sort()
if n<2:
    print(-1)
else:
    for i in range(len(arr)):
        print(arr[i]*arr[i+1])
        break
