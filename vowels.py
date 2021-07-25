# Python program to remove vowels from a string

def rem_vowel(string):
	vowels = ['a','e','i','o','u']
	result1 = [letter for letter in string if letter.lower() not in vowels]
	result = ''.join(result1)
	print(result)

string = input("Inter a string : ")
rem_vowel(string)


