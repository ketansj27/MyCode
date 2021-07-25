'''
Print an integer representing the number of data characters that do not 
change position even after the data stream is reversed. If no such 
character is found or the input string is empty then print 0.
'''
list1 = list()
list2 = list()
list3 = list()

string = input("inter string : ")

for letter in string :
    #print(letter)
    list1.append(letter)
    list2.append(letter)

#print(list1)
list2.reverse()
#print(list2)
n = -1
for letter in list1:
    #print("list 2 ",letter)
    n = n + 1
    let = list2[n]
    #print("list 2 ",let)
    if letter is let:
        list3.append(letter)

#print(list3)
print(len(list3))

    