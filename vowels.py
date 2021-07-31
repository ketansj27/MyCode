# Python program to remove vowels from a string

list1 = list()
string = input("Inter a string : ")

vowels = ['a','e','i','o','u']

for letter in string :
	if letter not in vowels:
		list1.append(letter)
#print(list1)
result = ''.join(list1)  # join the letter in list
print(result)
