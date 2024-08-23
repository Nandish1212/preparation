"""Problem statement
It is Edward's birthday today. His friends have bought him a huge circular cake.
Edward wants to find out the maximum number of pieces he can get by making exactly N straight vertical cuts on the cake.
Your task is to write a function that returns the maximum number of pieces that can be obtained by making N number of cuts.
Note: Since the answer can be quite large, modulo it by 1000000007
Input Specification:
input1: An integer N denoting the number of cuts
Anshika chaudhary
NEW YORK U.S.A
Output Specification:
Return the maximum number of pieces that can be obtained by making N cuts on the cake"""
n=int(input('Enter number of cuts:'))
result=n*(n+1)/2
print(int(result+1))