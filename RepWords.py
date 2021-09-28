'''
The online English language skills learning website 'EngAtTip' 
has designed an assessment. In the assessment a piece of text 
is displayed to the students. The text contains space separated 
words. A word is an alphabetic sequence of characters with no 
whitespaces in between the characters, The students must identify 
the words that are repeated in the text more than or equal to N 
times. These repeated words are automatically removed by the system 
before the next text in displayed to the students. The texts do 
not contain any punctuation marks.
Write an algorithm to display the words that are repeated more than 
or equal to Nomes in the text.

Example :
input  : cat batman latt matter cat matter cat cat latt latt
output : cat latt
Explanation :
The word "cat is repeated four times and the word "Matt" is repeated t
hree times in the next Hence the words that will be removed are [cat","latt).
'''
data = input()
repeat_time = int(input())
Words_list = list()
data  = data.split()
counts = dict()
for word in data:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] = counts[word] +  1

for key,value in counts.items() :
    if value >= repeat_time :
        Words_list.append(key)

if len(Words_list) == 0:
    print('NA')
else :
    print(*Words_list, sep =" ")
