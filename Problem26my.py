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

