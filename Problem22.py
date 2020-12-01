'''
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
'''

f=open('Problem22-names.txt')
names=str(f.read()).replace('"','').split(',')
names.sort()
position=' ABCDEFGHIJKLMNOPQRSTUVWXYZ' #Adding a whitespace to make the index number of alphabets same as its position in alphabet
sum=0
pos=1
for name in names:
    s=0 #Stores sum of alphabetic positions
    for alpha in name:
        s+=position.index(alpha)
    sum+=pos*s
    pos+=1

print("The total of all the name scores in the given file is ",sum)
    