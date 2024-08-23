string=input()
char=input()
output=''
for i in string:
    if i=='b':
        output+=char
    else:
        output+=i
print(output)