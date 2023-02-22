with open('17-304.txt') as f:
    a=[int(x) for x in f.readlines()]
a1=[]
a2=[hex(x)[2:].count('a') for x in a]
s=[x for x in a if x%120==0]
for i in range(len(a)-1):
    if a[i]>0 and a[i+1]>0:
        if a2[i]%2==0 and a2[i]>0 and a2[i+1]>0 and a2[i+1]%2==0 and (a[i]+a[i+1])>max(s):
            a1.append(a[i]+a[i+1])
print(len(a1),min(a1))