'''
In an online exam, the test paper set s categorized by the letters A-Z 
The students enrolled in the exam have been assigned a numeric value called 
application ID. To assign the test set to the student, firstly the sum of all 
digits in the application ID is calculated if the sum is within the numeric 
range 126 the corresponding alphabetic set code is assigned to the student, 
else the sum of the digits are calculated again and so on until the sum falls 
within the 1-26 range.
Write ad algorithm to display the examitation set code according to the student applican

Example 1
Input: 6442
Output: P
Explanation:
The sum of the digits of the application 6+4+4+2=16.
The letter that corresponds to 16 is P. Hence
the output is P.

Example 2
Input :558823
Output: D
Explanation :
The sum of the digits of the application ID is 5-5-8-8+2+3-31.
The letter that corresponds to 31 is none. Hence again the sum of 
digits are done The sum of the digits are 3+1.The letter that 
corresponds to 4 is D. Hence the output is D
'''
data = input()
sum = 0
Re_sum = 0
alpha = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

for num in data:
    num = int(num)
    sum = sum + num

if sum >= 1 and sum <= 26:
    print(alpha[sum -1])
else:
    sum = str(sum)
    for num in sum:
        num = int(num)
        Re_sum = Re_sum + num

print(alpha[Re_sum - 1])        