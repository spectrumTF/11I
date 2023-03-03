a=[int(x) for x in open('17-243.txt')]
a1=[]
b=[x for x in a if x%171==0]
c=max(b)
for i in range(len(a)-1):
    if (a[i]<c or a[i+1]<c) and (a[i]%2!=0 or a[i+1]%2!=0):
        a1.append(a[i]+a[i+1])
print(len(a1),max(a1))