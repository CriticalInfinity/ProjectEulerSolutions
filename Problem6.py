'''The sum of the squares of the first ten natural numbers is,

The square of the sum of the first ten natural numbers is,

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is .

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.'''

#We know that the sum of first n natural numbers is n(n+1)/2
#We also know that the sum of squares of first n natural numbers is [n(n+1)(2n+1)]/6

def Diff(n):
    sumOfSquares=  (n*(n+1)*(2*n+1))//6
    squareOfSum=((n*(n+1))//2)**2 
    return squareOfSum-sumOfSquares

print("The required difference is ",Diff(100))


