array=[1,4,6,27,8,19]
# print(max(array))
max_num=array[0]
for num in array:
    if num>max_num:
        max_num=num
print(max_num)