def f(x):
    c=0
    c1=0
    while x!=0:
        if x%10%2==0:
            c+=x%10
        else: c1+= x%10
        x//=10
    return c1>c
a=[int(x) for x in open('17-304.txt')]
a1=[]
s=[x for x in a if x%2==1]
for i in range(len(a)-1):
    if f(a[i])==True and f(a[i+1])==True and (a[i]+a[i+1])%min(s)==0:
        a1.append(a[i]+a[i+1])
print(len(a1),min(a1))