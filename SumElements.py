'''
In an online maths tutorial a student is given a list of N numbers. 
From this list, the student is required to sum each element in the 
list such that the ith element in the output list will be equal to 
the sum to the first element until the th element in the list.
Write an algorithm to calculate the sum of each element in the list.
Example

Input:  5
        14263
Output :1 5 7 13 16
Explanation :
The sum of each element 1, (1+4= 5), (1+4+2= 7), (1+4+2+6=13), (1+4+2+6+3=16)
Hence the output is 1 5 7 13 16
'''
numSize = input()
nums = str(input())
Asum = list()
nums = nums.replace(" ","")
sum = 0
for num in nums :
    sum = sum + int(num)
    #print(sum)
    Asum.append(sum)
print(*Asum,sep =" ")