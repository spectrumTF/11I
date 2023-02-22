with open('17-304.txt') as f:
    a=[int(x) for x in f.readlines()]
a1=[]
s=[x for x in a if x%123==0]
a2=[hex(x)[2:].count('b') for x in a]
for i in range(len(a)-1):
    if a2[i]%2==1 and a2[i+1]%2==1 and (a[i]+a[i+1])<max(s):
        a1.append(a[i]+a[i+1])
print(len(a1),max(a1))