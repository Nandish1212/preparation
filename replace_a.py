def replace_a(string):
    output=''
    for i in string:
        if i=='a':
            output+='b'
        elif i=='b':
            output+='a'
        else:
            output+=i
    return output

string=input()
print(replace_a(string))
