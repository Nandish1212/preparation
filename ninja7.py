string=input()
ch1=input()
ch2=input()
output=''
for i in string:
    if i==ch1:
        output=output+ch2
    elif i==ch2:
        output+=ch1
    else:
        output+=i
print(output)        
