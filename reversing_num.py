number=987654
number_string=str(number)
n=len(str(number))
for i in range(n-1,-1,-1):
    output=number_string[i]
    print(output, end='')


