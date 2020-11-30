'''
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
'''

def digitSum(n):
    sum=0
    while n>0:
        sum+=n%10
        n//=10
    return sum

def factorial(n):
    product=1 #Initializing product as 1. If we initialize it as 0 then any number multiplied by 0 is 0, therefore, the variable product will always have a value 0
    for x in range(1,n+1):
        product*=x
    return product

facto=factorial(100)
sum=digitSum(facto)

print("The sum of digits in the number 100! is ",sum)