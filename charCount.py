'''
During the fall season the Place Hill country receives lots of students visa 
applications for admissions in the various degree colleges of the country. 
The country code of all the visa applications received online per day is 
stored in the form of strings tagged 'a-z' or 'A-Z in the visa center database.
Each character of the string represents the country code. The string is case 
sensitive and lowercase letters represent one country and capital ters represent 
another country. The visa center wishes to know the count of the applications of 
a particular country code received per day.

Write an algorithm to help the visa center find out the count of the application 
of a particular country code received per day
Example :
Input: aBAboxydaAAA
        A
Output: 4

Explanation: The character A appears 4 times in the string. Hence the output is 4.
'''
Data = input()
char = input()
Total = 0
for letter in Data :
    if letter == char:
        Total = Total + 1

print(Total)