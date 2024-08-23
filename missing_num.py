def missing_num(arr):
    sum1=sum(arr)
    n=len(arr)
    sum2=(n*(n+1))/2
    return int(sum2-sum1)

arr=list(map(int,input().split()))
print(missing_num(arr))
