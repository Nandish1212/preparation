#make a row and the column 0 if 0 in the a row. 
arr=[[1,1,1],[1,0,1],[1,1,1]]
m=len(arr)
n=len(arr[0])
set_row=set()
set_col=set()
for i in range(m):
    for j in range(n):
        if arr[i][j]==0:
            set_col.add(j)
            set_row.add(i)

for i in set_row:
    for j in range(n):
        arr[i][j]=0
for i in set_col:
    for j in range(m):
        arr[j][i]=0
        
print(arr)
