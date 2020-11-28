'''
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
'''

# 1000=2*2*2*5*5*5

def SumOfDigits(n):
    sum=0
    while n>0:
        d=n%10
        n//=10
        sum+=d
    return sum

sum=SumOfDigits(2**1000)
print("The sum of digits of the number 2^1000 is ",sum)
