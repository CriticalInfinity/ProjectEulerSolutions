'''
Take the number 192 and multiply it by each of 1, 2, and 3:

192 × 1 = 192
192 × 2 = 384
192 × 3 = 576
By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?
'''
#since the pandigital number should consists of 9 digits and all digits from 1 to 9, therefore we are setting the limit at 1000//n such that we get 3 digits after multiplying it with numbers in range(1 to n)
def isPandigital(n):
    return len(n)==9 and not bool('123456789'.strip(n))
n=0
while n<=1:
    n=int(input("Enter the value of n(such that n>1): "))
largest=0
largest_f=0
for x in range(1,1000//n+1):
    st=''
    for y in range(1,n+1):
        st=st+str(x*y)
    if isPandigital(st):
        if largest<int(st):
            largest_f=x
            largest=int(st)

print("The largest pandigital number that can be formed as the concatenated product of an integer with (1,2,...,n) is",largest)
print("It is formed by the number",largest_f)