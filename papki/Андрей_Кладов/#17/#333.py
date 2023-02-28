a=[int(x) for x in open('17-333.txt')]
a1=[]
s=[x for x in a if x//10000==0 and  x//1000>0]
sr=sum(s)/len(s)
def f(x):
    c=0
    while x!=0:
        c+=x%10
        x//=10
    return c
for i in range(len(a)-1):
    if  not(a[i]+a[i+1] in a) and a[i]+a[i+1]<sr:
        a1.append(f(a[i])+f(a[i+1]))
print(len(a1),max(a1))