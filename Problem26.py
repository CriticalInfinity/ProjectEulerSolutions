'''
A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10	= 	0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
'''
def prime_sieve(n):#For finding primes
    sieve = [True] * (n//2)
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i//2]:
            sieve[i*i//2::i] = [False] * ((n-i*i-1)//(2*i)+1)
    return [2] + [2*i+1 for i in range(1,n//2) if sieve[i]]
print(prime_sieve(1000))
def f(N):
    if N < 8: return 3
    for d in prime_sieve(N)[::-1]:
        k = d//2
        while pow(10, k, d) != 1:  
             k+= 1
             if d-1 == k: 
                return d

N = int(input('The longest recurring cycle for 1/d where d < '))
d = f(N)
print ("The longest repeating decimal is for " ,d)