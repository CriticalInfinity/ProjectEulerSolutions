'''
The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
'''
cnt=0 #count
i=10
sum=0# holds sum
def IsPrime(num): #checks if a number is prime or not
    if num<=1:
        return False
    h=2
    while h*h<=num:
        if num%h==0:
            return False
        h+=1
    return True

while cnt<11:
    truncable=True#stores truncable status
    t=i
    while t>0:#checks if a number is left trucable
        if not(IsPrime(t)):#checks if t is prime
            truncable=False
            break
        t=t//10 #removes the last digit of t
    if not(truncable):#to skip following code if the number is not left truncabe
        i=i+1
        continue
    t=i
    x=t%10
    k=1
    while t>0:# checks whether the number is right trucable
        if not(IsPrime(x)):
            truncable=False
            break
        t=t//10
        x=x+t%10*(10**k)
        k+=1
    if not(truncable):#skips the following code if the number is not right trucable
        i+=1#increases the value of i by one
        continue
    sum=sum+i#if the number is trucable from both sides then the number is added to the sum
    cnt+=1#increases the counter
    i+=1
print("The sum is",sum)
