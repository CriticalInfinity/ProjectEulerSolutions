'''
Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

1634 = 1^4 + 6^4 + 34 + 4^4
8208 = 8^4 + 2^4 + 0^4 + 8^4
9474 = 9^4 + 4^4 + 7^4 + 4^4
As 1 = 1^4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
'''
'''
We need to find a number x9^5 which gives us an x digit number. 
Since 9^5 = 59049, we need at least 5 digits. 59^5 = 295245, so with 5 digits we can make a 6 digit number. 6*9^5 = 354294. 
So ,lets take the upper bound as 360000
'''
def digitToPower5(num):#to check if the sum of digits to the power of 5 is equal to the number itself
    digisum=0
    t=num
    while t>0:#extracting the digits and raising it to the power of five and adding it to digisum
        d=t%10
        t=int(t/10)
        digisum=digisum+(d**5)
    if digisum==num:
        return True
    return False
sum=0
for number in range(2,360000):
    if digitToPower5(number):
        sum=sum+number

print("The of all the number that can be written as the sum of fifth powers of their digits is",sum)
