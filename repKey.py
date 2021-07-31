'''
A company is transmitting data to another server. The data is in the form of numbers. 
To secure the data during transmission, they plan to obtain a security key that will be 
sent along with the data. The security key is identified as the count of the unique 
repeating digits in the data.

Input :The input consists of an integer data, representing the data to be transmitted.
Output : Print an integer representing the security key for the given data. If no data is 
        repeated it should display -1
Example :
Input: 578378923
Output: 3
Explanation
The repeated digits in the data are 7, 8 and 3. So, the security key is 3.
'''
data = int(input("inter data : "))  # transmitting data is in 'int' format.
data = str(data)                    # 'int' to 'str' for iteration purpose.
list1 = list()

counts = dict()
for digit in data:
        if digit not in counts:
            counts[digit] = 1
        else:
            counts[digit] = counts[digit] +  1
        
for key,value in counts.items() :
    #print(key,value)
    if value >= 2 :
        list1.append(key)           # this list will append repeated int

#print(counts)
#print(list1)
if (len(list1)) == 0:
    key = -1
else :
    key = (len(list1))

print(key)
