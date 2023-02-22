with open('17-299.txt') as f:
    a=[int(x) for x in f.readlines()]
a1=[]
def f(x):
    c=0
    while x!=0:
        c+=x%10
        x//=10
    return c
s=[f(x) for x in a if x%50==0]
for i in range(len(a)-2):
    if (a[i]==f(a[i+1]) or a[i]==f(a[i+2]) or a[i+1]==f(a[i]) or a[i+1]==f(a[i+2]) or a[i+2]==f(a[i+1]) or a[i+2]==f(a[i])) and a[i]+a[i+1]+a[i+2]<sum(s):
        a1.append(a[i]+a[i+1]+a[i+2])
print(len(a1),max(a1))