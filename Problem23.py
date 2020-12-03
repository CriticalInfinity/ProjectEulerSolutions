'''
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
'''

def SumOfProperFactors(n):
    sum=1
    if n==1:
        return 0
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

abundantNum=[]
#Since all number greater than 20162 can be written as the sum of two abundant number
#So it is not required to check numbers greater than 20162
def abundantNums():
    for x in range(12,20163): #Since 12 is the smallest abundant number we will start the loop from 12
        if x<SumOfProperFactors(x):
            abundantNum.append(x)

if 20160<SumOfProperFactors(20160):
    print("True")

abundantNums()
print(abun)
sum=1
arr=set(abundantNum) 
for n in range(2, 20162):
    flag = True
    for k in abundantNum:
        if k < n:
            if (n-k) in arr:
                flag = False
                break
        else: 
            break
    if flag: 
        sum += n




print("The sum of all positive intergers that cannot be written as the sum of two abundant numbers is ",sum)