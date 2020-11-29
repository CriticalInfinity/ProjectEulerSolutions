'''
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
'''

words=['one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen','twenty']
tens=['twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
def numInWords(n):
    word=""
    if n<=20:
        word+=words[n-1]
    if n>20 and n<100:
        word=tens[n//10-2]
        if n%10!=0:
            word=word+'-'+words[int(n%10)-1]
    if n>=100 and n<1000:
        word+=words[n//100-1]+" hundred "
        if n%100!=0:
            word=word+"and "+numInWords(n%100) #calling the function itself to generate last two digits in words 
    if n==1000:
        word='one thousand'
    return word

sum=0
for x in range(1,1001):
    sum+=len(numInWords(x).replace(" ","").replace("-",""))

print("The number of letter that would be used is ",sum)