def reverse_words(string):
    words=string.split(' ')
    output=''
    for i in range(len(words)-1,-1,-1):
        output+=words[i]+' '
    return output
string=input()
print(reverse_words(string))
