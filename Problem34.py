result=0
fact=[1]
for x in range(1,10):
    pro=1
    for y in range(2,x):
        pro*=y
    fact.append(pro)

for x in range(3,2540161):
    sum=0
    t=x
    while t>0:
        d=t%10
        t=t//10
        sum=sum+fact[d]
    if sum ==x:
        result+=x

print("The required sum is ",result)
