'''
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
'''

def isPrime(n):
    if n==1:
        return False
    if n%2==0:
        return False
    h=3
    while h*h<=n:
        if n%h==0:
            return False
        h+=2
    return True

def circular(n):
    s=str(n)
    # if len(s)>1 and (s.find('2')==0 or s.find('4')==0 or s.find('6')==0 or s.find('8')==0 or s.find('0')==0):
    #     return False
    for x in range(len(s)):
        s=s[1:]+s[0]
        if not isPrime(int(s)):
            return False
    return True
cnt=0
for num in range(2,10**6):
    if isPrime(num):
        if circular(num):
            cnt+=1
print("The number of circular primes under one million is ",cnt)