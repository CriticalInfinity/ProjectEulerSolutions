'''
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
'''
seqLength={}

def Collatzseq(n):
    cnt=1 #Counting one also
    t=n
    while n!=1:
        if n%2==0:
            n=n//2
            if n in seqLength:
                cnt=cnt+seqLength[n]
                break
        else: 
            n=3*n+1
            if n in seqLength:
                cnt=cnt+seqLength[n]
                break
        cnt+=1        
    seqLength[t]=cnt
    return cnt

num=0 #Stores the number which has the longest chain
ch=0 #Stores the longest chain's length
for x in range(1,10**6):
    chainLength=Collatzseq(x)
    if chainLength>ch: #checks whether the chainlength of current number is greater than the previous ones
        num,ch=x,chainLength 

print("Longest chain length: ",ch)
print("The number with the longest chain which is under one million is ",num)