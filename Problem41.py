'''
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
'''
n=int(input("Enter the value of n: "))
limit=10**n-1
primes=[True]*(limit+1)
primes[0],primes[1]=False,False
def isPandigital(num,n):
    return len(str(num))==n and not("1234567890"[:n].strip(str(num)))

def SieveOfEratosthenes(limit,n):
    h=2
    while h*h<=limit:
        if primes[h]:
            for i in range(h*h,limit+1,h):
                primes[i]=False
        h+=1
SieveOfEratosthenes(limit,n)
max=0
for i in range(len(primes)):
    if primes[i]:
        if isPandigital(i,n):
            max=i
print(f"The largest {n}-digit pandigital primes number is {max}")