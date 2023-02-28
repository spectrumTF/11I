a=[int(x) for x in open('17-316.txt')]
a1=[]
sr=sum(a)/len(a)
def f(x,y):
    c=[]
    c1=[]
    while x!=0:
        c.append(x%10)
        c1.append(y%10)
        x//=10
        y//=10
    return c[0]+c1[0]==c[3]+c1[3]
for i in range(len(a)-2):
    sr1=(a[i]+a[i+1]+a[i+2])/3
    if (f(a[i],a[i+1])==True or f(a[i+2],a[i+1])==True or f(a[i],a[i+2])==True) and sr1>sr :
        a1.append(a[i]+a[i+1]+a[i+2])
print(len(a1),max(a1))