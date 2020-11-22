'''A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.'''

def isPalindrome(number):
    t=number
    rev_num=0
    while t>0:#For reversing a number
        d=t%10
        t//=10
        rev_num=rev_num*10+d
    if number==rev_num:# checks if the reverse of the number is equal to the number itselfz
        return True
    return False

largest=0
for x in range(999,99,-1):
    for y in range(x,1000):
        if isPalindrome((x*y)):
            if x*y>largest:
                largest=x*y
                

print("The required largest palindrome number is ",largest)