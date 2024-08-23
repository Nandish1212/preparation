"""In an array a superior element is one which is greater than all the elements to its right side. The rightmost element itself be a superior element.
You are given a function, int Find_Number_Of_Superior_Element(int arr[], int n);
The function accepts an integer array and the size of array, Implement the function to find the total number of superior elements present in array.
Assumptions:
N>0 and Array index starts from 0
Input: n= 6
arr= [8,10,6,2,9,7]
Output: 3
12345
"""""


arr=[8,6,2,7,10]
n=len(arr)
max_rigth=arr[n-1]
count=1
for i in range(n-2,-1,-1):
    if arr[i]>max_rigth:
        count+=1
        max_rigth=arr[i]
print(count)

