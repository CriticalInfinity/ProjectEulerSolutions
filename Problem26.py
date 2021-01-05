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

def sieveprime(n): #Finds all primes less than n
    primes=[True]*(n//2) # We are not checking the even numbers to reduce the number of loops. So we are initializing it with True for all indices because there lies n//2 odd numbers below n
    for x in range(3,int(n**0.5)+1,2):
        if primes[x//2]:
            primes[(x*x)//2::x]=[False]*((n-x*x-1)//(2*x)+1)
    return [2]+[2*i+1 for i in range(1,n//2) if primes[i]]

def rec(n):
    if n<=7:
        return 3
    primes=sieveprime(n)#Calling the function and reversing the list 
    primes.reverse()
    for x in primes:
        z=x//2
        while pow(10,z,x)!=1:
            z+=1
        if x-1==z:
            return x

n=1000
num=rec(n)
print("The longest repeating decimal less than 1000 is ",num)

