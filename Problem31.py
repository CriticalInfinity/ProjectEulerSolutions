'''
In the United Kingdom the currency is made up of pound (£) and pence (p). There are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).
It is possible to make £2 in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?
'''
ways=0
coins=[200,100,50,20,10,5,2,1] #stores all different kinds of denominations
def denomination(deno,target,j):
    global ways #to make the value of ways global
    for i in range(target,-1,-deno):#runs from target to 0 and step is -deno
        if deno==2:#base case
            ways+=1
        else:
            denomination(coins[j],i,(j+1))
denomination(coins[0],200,1)
print("The number of ways is",ways)