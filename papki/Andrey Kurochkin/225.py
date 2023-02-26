def f(x):
    a=0
    while x > 0:
        if x%10==1:
            a+=1
        x//=10
    if a!=0:
        return 1
    else:
        return 0
a = [int(x) for x in open("17-4.txt")]
c = []
s = sum(a)/len(a)
for i in range(len(a)-1):
    if (a[i]<s or a[i+1]<s) and (f(a[i])==1 and f(a[i+1])==1):
        c.append(a[i]+a[i+1])
print(len(c),min(c))
