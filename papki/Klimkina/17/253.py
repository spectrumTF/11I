a=[int(x) for x in open('17-243.txt')]
a1=[]
b=[x for x in a if x%127==0]
c=max(b)
for i in range(len(a)-1):
    if (a[i]>c or a[i+1]>c) and (oct(a[i]).count('31')>=1 or oct(a[i+1]).count('31')>=1):
        a1.append(a[i]+a[i+1])
print(len(a1),min(a1))