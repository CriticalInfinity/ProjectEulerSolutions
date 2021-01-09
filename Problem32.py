'''
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
'''

pandigitals=set()
def genpandigital():
    for x in range(2,99):
        y=x+1
        while x*y<9999:
            y=y+1
            if len(str(x)+str(y)+str((x*y)))==9 and not '123456789'.strip(str(x)+str(y)+str((x*y))):
                pandigitals.add(x*y)

genpandigital()
print("The sum is ",sum(pandigitals))