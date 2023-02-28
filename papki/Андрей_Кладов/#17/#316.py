a=[int(x) for x in open('17-316.txt')]
a1=[]
def f(x,y):
    c=0
    while x!=0:
        if x%10!=y%10:
            c+=1
        x//=10
        y//=10
    return c==1
for i in range(len(a)-2):
    if (f(a[i],a[i+1])==True or f(a[i+2],a[i+1])==True or f(a[i],a[i+2])==True) and a[i]+a[i+1]+a[i+2]<9999+9996:
        a1.append(a[i]+a[i+1]+a[i+2])
print(len(a1),min(a1))