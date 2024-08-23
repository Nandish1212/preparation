def occurence_count(arr,ele):
    count=0
    for i in arr:
        if i==ele:
            count+=1
    if count==0:
        return 'Element not found in list!'
    return count
arr=list(map(int,input().split()))
ele=int(input())
print(occurence_count(arr,ele))
