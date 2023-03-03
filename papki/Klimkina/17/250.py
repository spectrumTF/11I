a=[int(x) for x in open('17-243.txt')]
a1=[]
b=[x for x in a if x%171==0]
c=max(b)
for i in range(len(a)-1):
    if (a[i]>c or a[i+1]>c) and (str(a[i]).count('11')>=1 or str(a[i+1]).count('11')>=1):
        a1.append(a[i]+a[i+1])
print(len(a1),min(a1))