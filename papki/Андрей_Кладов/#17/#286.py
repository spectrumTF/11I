def f(x):
    c=0
    while x!=0:
        c+=x%10
        x//=10
    return c
a=[int(x) for x in open('17-282.txt')]
a1=[]
s=[f(int((oct(x)[2:]))) for x in a]
s1=[x for x in a if x%21==0]
x=f(int((oct(min(s1))[2:])))
for i in range(len(s)-1):
    if s[i]==x or s[i+1]==x:
        a1.append(a[i]+a[i+1])
print(len(a1),min(a1))