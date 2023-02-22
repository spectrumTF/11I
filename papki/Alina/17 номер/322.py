with open('17-316.txt') as f:
    a=[int(x) for x in f.readlines()]
a1=[]
def f(x,y):
    sa=(x+y)/2
    sg=(x*y)**0.5
    return sa==int(sa) and sg==int(sg)
for i in range(len(a)-2):
    if (f(a[i],a[i+1])==True or f(a[i+2],a[i+1])==True or f(a[i],a[i+2])==True) and a[i]+a[i+1]+a[i+2]<9999+9996:
        a1.append(a[i]+a[i+1]+a[i+2])
print(len(a1),min(a1))