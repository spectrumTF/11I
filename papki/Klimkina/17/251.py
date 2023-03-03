a=[int(x) for x in open('17-243.txt')]
a1=[]
b=[x for x in a if x%153==0]
c=max(b)
for i in range(len(a)-1):
    if (a[i]>c or a[i+1]>c) and (bin(a[i])[2:].count('1111')>=1 or bin(a[i+1])[2:].count('1111')>=1):
        a1.append(a[i]+a[i+1])
print(len(a1),min(a1))