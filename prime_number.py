#Checking weather the number is prime or not a prime.!

import math
def prime_number(n):
    if n<=3:
        return f'Given {n} is prime number'
    sqrt_n=math.sqrt(n)
    for i in range(2,int(sqrt_n)+1):
        if n%i==0:
            return f'Given {n} is not a prime number'
    return f'Given {n} is prime number'
n=int(input())
print(prime_number(n))
