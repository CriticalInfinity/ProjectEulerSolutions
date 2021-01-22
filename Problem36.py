'''
The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
'''

def dec2bin(dec):
    s=''
    while dec>=1:
        s=s+str(dec%2)
        dec=dec//2
    return int(s[::-1])

def isPalindromic(num):
    if str(num)[::-1]==str(num):
        return True
    return False

sum=0
n=10**6
for num in range(1,n+1):
    if isPalindromic(num) and isPalindromic(dec2bin(num)):
        sum+=num

print("The sum of numbers palindromic in base 10 and base 2 is ",sum)
        
        