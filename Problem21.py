'''
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
'''
limit=10000
list1=[x for x in range(1,limit)]

def AmicableNum(n):
    s1=SumOfProperFactors(n)
    s2=SumOfProperFactors(s1)
    if s2==n and n!=s1 and s2<limit: #n!=s1 to prevent the program to add the number themselves like n=6 then s1=6 then the number is not amicable because it is the number itself
        list1.remove(s1)
        return n+s1
    return 0

def SumOfProperFactors(n):
    sum=1
    i=2
    while i*i<=n:
        if n%i==0:
            l=n//i
            if i%2==0 or l%2==0:
                if l==i: 
                    sum+=i
                else:
                    sum+=i+l
        i+=1            
    return sum
sum=0
from time import time
start=time()
for x in list1:
    sum+=AmicableNum(x) 

print("The sum is ",sum)