'''
A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10	= 	0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
'''
from math import sqrt

limit=int(input("Enter the limit under which you want to find the longest recurring cycle \n"))

length=0 #Stores the length of the longest recurring cycle
num=0

def PrimeChecker(n):
    if n==1:
        return False
    for x in range(2,int(sqrt(n))+1):
        if n%x==0:
            return False
    return True

primes=[]
for x in range(2,limit):
    if PrimeChecker(x):
        primes.append(x)
primes.reverse()

for x in primes:
    if length>x:
        break
    rem=[0 for y in range(x)]
    val=1
    pos=0
    while rem[val]==pos and val!=0:
        rem[val]=pos
        val*=10
        val%=x
        pos+=1
    if pos-rem[val]>length:
        length=pos-rem[val]
        num=x

print(num," is the number with the longest recurring cycle")