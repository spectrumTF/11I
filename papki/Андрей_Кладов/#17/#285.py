def f(x):
    c=0
    while x!=0:
        c+=x%10
        x//=10
    return c
a=[int(x) for x in open('17-282.txt')]
a1=[]
s=[x for x in a if x%37==0]
for i in range(len(a)-1):
    if f(a[i])==f(min(s)) or f(a[i+1])==f(min(s)):
        a1.append(a[i]+a[i+1])
print(len(a1),min(a1))