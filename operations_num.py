""")18 Sept 2023(کا Given a number N your Task is to make N a single digit number by performing these operations
1) If N is odd make it floor (N/2)
2) If N is even, make it floor((N-2)/2)
3) If N is already a single digit, print as it is
Example:
Input 1: N=25
Output 1: 12
Input 2: N=10
Output: 4
Input 3: N=5
Output: 5
NEW YO S.A
"""

n=int(input('Enter the number:'))
result=0
if len(str(n))==1:
    print(n)
else:
    if n%2==0:
        result=(n-2)/2
        print(result)
        
    else:
        result=n//2
        print(result)