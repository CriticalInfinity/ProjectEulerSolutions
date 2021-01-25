'''
The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
'''
import time
a={1,2,3,5,7,9}
cnt=0
i=10
sum=0
def IsPrime(num):
    if num==1:
        return False
    h=2
    while h*h<=num:
        if num%h==0:
            return False
        h+=1
    return True

while cnt<11:
    truncable=True
    t=i
    while t>0:
        if not(IsPrime(t)):
            truncable=False
            break
        t=t//10
    if not(truncable):
        i=i+1
        continue
    t=i
    x=t%10
    k=1
    while t>0:
        if not(IsPrime(x)):
            truncable=False
            break
        t=t//10
        x=x+t%10*(10**k)
        k+=1
    if not(truncable):
        i+=1
        continue
    sum=sum+i
    cnt+=1
    i+=1
print("The sum is",sum)
