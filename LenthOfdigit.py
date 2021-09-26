'''
Given two positive numbers N and K The task is to find the number N 
contains exactly K digit or not. If contains then print True<space><digit 
count of N> Otherwise, print False<space><digit count of N>

Example 1:
Input:501
3
Output: True 3

Example 2:
Input: 50121
4 
Output: False 5

'''
Nvalue = input()
Kvalue = input()
#print(Nvalue)
Nvalue = Nvalue.strip("0")
#print(Nvalue)
Nvalue = str(Nvalue)
count = 0
for value in Nvalue :
    count = count +1
#print(count)
if count == Kvalue:

    print("True",Kvalue)
else:
    print("Flase",Kvalue)