with open('17-316.txt') as f:
    a=[int(x) for x in f.readlines()]
a1=[]
def f(x):
    c=set()
    while x!=0:
        c.add(x%10)
        x//=10
    if len(c)==10:   
        return True
    else: False
def fa(x):
    c=0
    while x!=0:
        c+=x%10
        x//=10
    return c
a2=[fa(x) for x in a]
for i in range(len(a)-2):
    if f(a[i]*a[i+1]*a[i+2])==True and a[i]+a[i+1]+a[i+2]<sum(a2):
        a1.append(a[i]+a[i+1]+a[i+2])
print(len(a1),min(a1))