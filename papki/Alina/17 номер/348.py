with open('17-346.txt') as f:
    a=[int(x) for x in f.readlines()]
from fnmatch import*
a1=[]
def f(x):
    c=1
    while x!=0:
        c*=x%10
        x//=10
    return c    
for i in range(len(a)-2):
    if  f(a[i])*f(a[i+1])*f(a[i+2])<=2*10**9 and fnmatch(str(f(a[i])*f(a[i+1])*f(a[i+2])),'55*2*')==True:
        a1.append(f(a[i])*f(a[i+1])*f(a[i+2]))
print(len(a1),max(a1))