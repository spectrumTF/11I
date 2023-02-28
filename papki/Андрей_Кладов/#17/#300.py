def f(x):
    c=0
    while x!=0:
        c+=x%10
        x//=10
    return c
a=[int(x) for x in open('17-302.txt')]
a1=[]
s=[x for x in a if x%401==0]
for i in range(len(a)-2):
    if (a[i]%(f(a[i+1])+f(a[i+2]))==0 or a[i+1]%(f(a[i])+f(a[i+2]))==0 or a[i+2]%(f(a[i+1])+f(a[i]))==0) and a[i]+a[i+1]+a[i+2]>max(s):
        a1.append(a[i]+a[i+1]+a[i+2])
print(len(a1),min(a1))