with open('17-295.txt') as f:
    a=[int(x) for x in f.readlines()]   
a1=[]
def f(x):
    c=1
    while x!=0:
        c*=x%10
        x//=10
    return c
for i in range(len(a)-1):
    if f(a[i]+a[i+1])>0:
        if (a[i]+a[i+1])%f(a[i]+a[i+1])==0 and (a[i]+a[i+1])<max(a):
            a1.append(a[i]+a[i+1])
print(len(a1),max(a1))