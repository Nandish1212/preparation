def anagram(string1,string2):
    # output=False
    
    # for i in string1:
    #     if i in string2:
    #         output=True
    #     else:
    #         output=False
    # return output    
    return sorted(string1)==sorted(string2)
string1=input()
string2=input()
print(anagram(string1,string2))