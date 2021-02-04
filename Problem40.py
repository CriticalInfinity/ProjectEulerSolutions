'''
An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
'''
i=1
d=1
cnt=0
pro=1
while d<=1000000:
    cnt+=len(str(i))
    if cnt>=d:
        pro*=int(str(i)[-(cnt-d+1)])
        d=d*10
    i+=1
print("The product is",pro)