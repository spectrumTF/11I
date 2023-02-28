def f(x):
    c=0
    while x!=0:
        c+=x%10
        x//=10
    return c

a=[int(x) for x in open('17-302.txt')]
a1=[]
s=[f(x) for x in a if x%12==0]
for i in range(len(a)-2):
    if (int(a[i]%(f(a[i+1])+f(a[i+2]))==0) + int(a[i+1]%(f(a[i])+f(a[i+2]))==0) + int(a[i+2]%(f(a[i+1])+f(a[i]))==0))==1 and a[i]+a[i+1]+a[i+2]<sum(s):
        a1.append(a[i]+a[i+1]+a[i+2])
print(len(a1),max(a1))