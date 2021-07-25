'''
A company is transmitting data to another server. The data is in the form of numbers. 
To secure the data during transmission, they plan to obtain a security key that will be 
sent along with the data. The security key is identified as the count of the unique 
repeating digits in the data.
'''
data = input("inter data : ")
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
        list1.append(key)

   
#print(counts)
#print(list1)
print(len(list1))