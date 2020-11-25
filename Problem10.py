'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''

#This is a simple technique
'''def Prime(num):
    for x in range(2,num//2):
        if num%x==0:
            return False
    return True

sum=0
for y in range(2,2*10**6):
    if Prime(y):
        sum+=y

print("The sum is ",sum)
'''

#This is the fastest technique
num=2*(10**6)
primes=[True for x in range(num+1)]
primes[1]=False # 1 is not a prime number 
n=2
while n*n<=num:
    if primes[n]==True:
        for y in range(n*n,num+1,n):
            primes[y]=False
    n+=1

sum=0
for z in range(num+1):
    if primes[z]:
        sum+=z

print("The sum is ",sum)



        