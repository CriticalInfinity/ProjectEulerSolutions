'''2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?'''

#So we know that the smallest number that is divisible by each of the number from 1 to 10 is 2520
#Then the smallest positive number that is evenly divisible by all of the numbers from 1 to 20 should be a multiple of 2520
#Since 2520 is divisible by each number from 1 to 10, its multiples should also be divisible by each number from 1 to 10
#Therefore we are going to choose whether its multiples are divisible by each of the numbers from 11 to 20


flag=False
x=2

while not flag:
    flag=True
    multiple=x*2520
    for y in range(11,21):
        if multiple%y!=0:
            flag=False
            break
    x+=1


print("The smallest number that is divisible by each of the number from 1 to 20 is ",multiple)
    