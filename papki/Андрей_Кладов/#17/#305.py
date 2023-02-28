def f(x):
    c=''
    while x!=0:
        c+=str(x%8)
        x//=8
    return c[::-1]
a=[int(x) for x in open('17-304.txt')]
a1=[]
sr=sum(a)/len(a)
for i in range(len(a)-1):
    if (len(f(a[i]))%2==1 or len(f(a[i+1]))%2==1) and (a[i]+a[i+1])>sr:
        a1.append(a[i]+a[i+1])
print(len(a1),min(a1))