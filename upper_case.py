# Given a string you are requested to determine whether the string should be converted to all uppercase or all lowercase, depending on the count of uppercase and lowercase letter in that string.
# Example 1:
# AbCdEfG
# Output 1:
# ABCDEFG
# Example 2: 
# xYz
# Output 2:
# xyz
s=input()
upper_count=0
lower_count=0
for i in s:
    if i.isupper():
        upper_count+=1
    else:
        lower_count+=1
print(upper_count,lower_count)
if upper_count>lower_count:
    print(s.upper())
else:
    print(s.lower())
    