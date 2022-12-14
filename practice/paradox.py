import random
def monty(t):
    viborp=0
    a=[0,1,0]
    viborv=0
    for i in range(t):
        i=+1
        a=[0,1,0]
        n=random.choice(a)
        a.remove(n)
        if n==1:
            viborp+=1
            viborv+=1
        a.remove(0)
        if a[0]!=1:
            viborp+=1
    return round((viborp/t*100),3),round((viborv/t*100),3)
if 1==1:
    print(monty(100))