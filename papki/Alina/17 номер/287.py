with open('17-282.txt') as f:
    a=[int(x) for x in f.readlines()]   
def f(x):
    c=0
    while x!=0:
        c+=x%3
        x//=3
    return c
a1=[]
s1=[x for x in a if x%11==0]
x=f(max(s1))
for i in range(len(a)-1):
    if f(a[i])==x or f(a[i+1])==x:
        a1.append(a[i]+a[i+1])
print(len(a1),min(a1))  