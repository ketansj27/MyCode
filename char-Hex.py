'''
The delivery requests of an e-commerce website are depicted in the form of 
strings tagged 'a-z' or 'A-Z'. Each character of the string represents the 
request code. The ascii value of the character represents the number of products 
that need to be delivered for rat respective code. Due to limited delivery 
windows, the website has decided to deliver the products whose codes represents 
1the largest and the smallest ascii values in the string. The company needs to 
find out the total number of products delivered.
Write an algorithm to find out the total number of products delivered.

Input :
The input consists of a string-requestString representing the delivery request

Output :
Print an integer representing the total number of products delivered.

Example :
Input : aAklip

Output : 173

Explanation: 
The ascii value of the characters in the string are as follows:
a = 97
A = 65
k = 107
I = 108
i = 105
P = 80
The sum of the smallest and the largest ascli values is 65 + 108 = 173.
Hence the output is 173.
'''
string = input()
CharHex = list()

for char in string :
    CharHex.append(ord(char))
    
print(max(CharHex) + min(CharHex))