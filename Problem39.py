'''
If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
'''
def Solutions(limit):
    cnt=0
    for a in range(1,limit//3):
        for b in range(1,limit//2):
            c=limit-a-b
            if c<0:
                break
            if a**2+b**2==c**2:
                cnt+=1
    return cnt
import time
start=time.time()
diff=time.time()-start
print("Time taken:",diff)
max=0
max_solutions=0
for p in range(1,1001):
    s=Solutions(p)
    if s>max_solutions:
        max=p
        max_solutions=s

print("The maximum number of solutions is given by p={}".format(max))