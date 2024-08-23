def sqrt_odd_even_diff(m,n):
    sum_even=0
    sum_odd=0
    for i in range(m,n+1):
        if i%2==0:
            sum_even+=pow(i,2)
        else:
            sum_odd+=pow(i,2)
    return abs(sum_even-sum_odd)


m=int(input())
n=int(input())
print(sqrt_odd_even_diff(m,n))
