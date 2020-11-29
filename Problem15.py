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
#We would take 20 steps to the right and 20 steps in the downwards direction
#Let us write one of the path in symbols. R-right D-Down
#RRRRRRRRRRRRRRRRRRRRDDDDDDDDDDDDDDDDDDDD  ____(1)
#This path is covered by going to the extreme right and then to the bottm
#Other paths are a variation of these steps
#Using the permutation formula for multiple objects of same type. Formula: n!/(p!*q!)
#where n is the total number of objects, p is the number of objects on one type, q is the number of objects of the other type
#Here R and D occuring 20 times in word (1) and the total number of letters is 40
#The answer is 40!/(20!*20!)
n=20
length=n*2
numPaths=nCr(length,n)
print("The number of paths are ",numPaths)
