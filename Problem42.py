'''
The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, how many are triangle words?
'''

alpha=" ABCDEFGHIJKLMNOPQRSTUVWXYZ" #to get the position of alphabet
file=open('words.txt','r') #opens file
words=str(file.readline()).replace("\"","").split(",")#reading the file and storing word in a list
max=0#stores the length of the longest word in the list "words"
for word in words:
    if len(word)>max:
        max=len(word)
triangle=[] #stores triaglue numbers
n=1
while ((n*(n+1))//2)<=(max*26):
    triangle.append((n*(n+1))//2)
    n+=1
cnt=0 #counter
for word in words:
    sum=0
    for char in word:
        sum+=alpha.index(char)
    if sum in triangle:
        cnt+=1
print("The number of triangle words are",cnt)