with open('17-328.txt') as f:
    a=[int(x) for x in f.readlines()]
a1=[]
def f(x):
    c=0
    while x!=0:
        if x%8%2==1:
            c+=1
        x//=8
    return c==0
def fa(x):
    c=0
    while x!=0:
        c+=x%10
        x//=10
    return c 
s=[fa(x) for x in a if x%22==0]
for i in range(len(a)-2):
    a2=[a[i]+a[i+1],a[i]+a[i+2],a[i+1]+a[i+2]]
    if f(a2[0])==True and f(a2[1])==True and f(a2[2])==True and a[i]+a[i+1]+a[i+2]<sum(s) :
        a1.append(a[i]+a[i+1]+a[i+2])
print(len(a1),min(a1))