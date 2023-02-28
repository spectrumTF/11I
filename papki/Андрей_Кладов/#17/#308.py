def f(x):
    c=0
    c1=0
    while x!=0:
        if x%10%2==0:
            c+=1
        else: c1+=1
        x//=10
    return c==c1
a=[int(x) for x in open('17-304.txt')]
a1=[]
for i in range(len(a)-1):
    if f(a[i])==True and f(a[i+1])==True and (a[i]+a[i+1])>max(a):
        a1.append(a[i]+a[i+1])
print(len(a1),max(a1))