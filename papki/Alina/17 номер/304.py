with open('17-304.txt') as f:
    a=[int(x) for x in f.readlines()]
a1=[]
def f(x):
    c=0
    while x!=0:
        c+=x%8
        x//=8
    return c    
for i in range(len(a)-1):
    if (int(a[i]%f(a[i+1])==0) + int(a[i+1]%f(a[i])==0))==1 and (a[i]+a[i+1])%min(a)==0 :
        a1.append(a[i]+a[i+1])
print(len(a1),max(a1))