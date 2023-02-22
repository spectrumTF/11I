with open('17-298.txt') as f:
    a=[int(x) for x in f.readlines()]
a1=[]
s=[x for x in a if x%197==0]
def f(x):
    c=[]
    while x!=0:
        c.append(x%10)
        x//=10
    return c
for i in range(len(a)-1):
    if (int((a[i]/197) in f(a[i])) + int(((a[i+1]/197) in f(a[i+1]))))==1 and (a[i]+a[i+1])<max(s):
        a1.append(a[i]+a[i+1])
print(len(a1),max(a1))        
            
            