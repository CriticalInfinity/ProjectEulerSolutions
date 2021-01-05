'''
Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
'''

import numpy as np

while True:
    try:
        n=int(input("Enter the dimension of the matrix: "))
        break
    except ValueError:
        print("You cannot enter a float value or a character at this input field. \nTry Again")
arr=np.zeros((n,n),dtype='i1')
matrix=arr.tolist()
del np
i=n*n
# #For creating a reverse spiral matrix
# c=n
# for x in range(int(n/2+1)):
#     for urow in range(n-c,c):#for upper row
#         matrix[x][urow]=i
#         i=i-1
#     for rcol in range(n-c+1,c): #for right column
#         matrix[rcol][c-1]=i
#         i=i-1
#     for drow in range(c-2,n-c-1,-1):#for the bottom row
#         matrix[c-1][drow]=i
#         i=i-1
#     for lcol in range(c-2,x,-1):#for left column of the square
#         matrix[lcol][n-c]=i
#         i=i-1
#     c=c-1

#For creating a spiral matrix
for x in range(int(n/2+1)):
    for urow in range(n-x-1,x-1,-1):
        matrix[x][urow]=i
        i=i-1
    for lcol in range(x+1,n-x):
        matrix[lcol][x]=i
        i=i-1
    for drow in range(x+1,n-x):
        matrix[n-x-1][drow]=i
        i=i-1
    for rcol in range(n-x-2,x,-1):
        matrix[rcol][n-x-1]=i
        i=i-1

sum=0
for rd in range(n):#for right diagonal
    sum+=matrix[rd][rd]
for ld in range(n-1,-1,-1):#for left diagonal
    sum+=matrix[n-ld-1][ld]
sum=sum-matrix[int(n/2)][int(n/2)] #removing the middle most element because it occurs twice in the sum
print("The sum is",sum)