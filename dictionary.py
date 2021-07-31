'''
A company Dictory is launching a new dictionary application for mobile users. 
Initially. the dictionary will not have any words. Instead it will be an 
auto-learning application that will learn according to a user's given text. 
When a user types text, the application auto-detects the words that appear 
more than once. T application then stores these words in the dictionary and 
uses them as suggestions in future typing sessions.

Write an algorithm to identify which words will be saved in the dictionary.

Input :
The input consists of a string textinput, representing the text that is given 
as an input to the application by the user.

Output
Print space-separated strings in the lexicographically sorted order representing
the number of repeated words detected in the input text and if no word is repeated 
print "NA".

Note :
A word is an alphabetic sequence of characters having no whitespace and there is 
no punctuation in the input text. textinput is case-sensitive (i.e. cat and CAT 
are considered as different words not same). It contains lowercase and uppercase 
English alphabets[i.e. a-z, A-Z].

Example
Input: cat batman latt matter cat matter cat
Output: cat matter
'''

data = input("data : ")
data = data.split()
#print(data)
counts = dict()
repWords = list()
for word in data:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] = counts[word] +  1
        
for key,value in counts.items() :
    #print(key,value)
    if value >= 2 :
        repWords.append(key)

#print(repWords)
print(' '.join(repWords))