'''By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?'''

cnt=0
#We are starting from 2 because 1 is neither a composite number nor a prime number
i=1 #I am initializing it as 1 because when the loop will start running then the value of i increases by 1 and becomes 2 
while cnt!=10001:
    i+=1
    flag=True
    for x in range(2,i//2+1):
        if i%x==0:
            flag=False
            break
    if flag:
        cnt=cnt+1
    
print("The 10001st prime number is ",i)