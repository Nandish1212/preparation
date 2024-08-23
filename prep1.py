n=int(input())
m=int(input())
sum_div_n=0
sum_not_div=0
for i in range(1,m+1):
    if i%n==0:
        sum_div_n+=i
    else:
        sum_not_div+=i
print(abs(sum_div_n-sum_not_div))