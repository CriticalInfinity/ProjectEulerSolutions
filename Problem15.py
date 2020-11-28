'''
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.


How many such routes are there through a 20×20 grid?
'''

#https://www.youtube.com/watch?v=JLIjzS-VGy4 Watch this video for an amazing explanation about this problem

import math
def nCr(n,r):
    f=math.factorial
    return f(n)//(f(r)*f(n-r))

#The path lenght is 20+20(20 in right/down direction)
n=20
length=n*2
numPaths=nCr(length,n)
print("The number of paths are ",numPaths)
