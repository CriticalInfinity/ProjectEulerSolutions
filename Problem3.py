'''The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?'''

n=600851475143
prime=2 # starting from 2 otherwise it will cause the loop to infinitely run because every number is can be divided by 1 for ever
while prime**2<n:
    while n%prime==0:
        n=n/prime
    prime+=1


print("The largest prime factor is ",int(n))

