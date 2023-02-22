with open('17-343.txt') as f:
    a=[int(x) for x in f.readlines()]
a1=[]
def f(x):
    d=0
    c=0
    c1=0
    while x!=0:
        if d%2==0:
            c1+=x%10
        else: 
            c+=x%10
        d+=1
        x//=10
    if c1>0:    
        return c%c1==0 
for i in range(len(a)-2):
    if  f(a[i])==True and f(a[i+1])==True and f(a[i+2])==True:
        a1.append(a[i]+a[i+1]+a[i+2])
print(len(a1),min(a1))