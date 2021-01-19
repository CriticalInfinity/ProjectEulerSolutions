'''
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
'''
import time
fractions=[]
for x in range(10,100):
    for y in range(x+1,100):
        num=str(x).strip(str(y))
        deno=str(y).strip(str(x))
        try:
            if int(num)/int(deno)==(x/y) and not(int(num)==x) and not(x%10==0):
                print(x)
                print(y)
                fractions.append([x,y])
        except:
            pass
print(fractions)
def lowest(n,d):#where n is numerator and d is denominator
    if n>d:
        max=n
    else:
        max=d
    for x in range(2,max):
        while (n%x==0 and d%x==0):
            n=n//x
            d=d//x
    return [n,d]
prod=1
pron=1
for nums in fractions:
    low=lowest(nums[0],nums[1])
    prod*=low[1]#Product of denominator
    pron*=low[0]#Product of numerator
low=lowest(pron,prod)
prod=low[1]
pron=low[0]
print("The product is ",prod)

