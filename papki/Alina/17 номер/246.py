with open('17-243.txt') as f:
    a=[int(x) for x in f.readlines()]
a1=[]
s=[x for x in a if x%171==0]
m=max(s)
for i in range(len(a)-1):
    if (a[i]<m or a[i+1]<m) and (a[i]%2==1 or a[i+1]%2==1):
        a1.append(a[i]+a[i+1])
print(len(a1),max(a1))        