a=[int(x) for x in open('17-243.txt')]
a1=[]
s=[x for x in a if x%171==0]
m=max(s)
for i in range(len(a)-1):
    if (a[i]>m or a[i+1]>m) and ('11' in str(a[i]) or '11' in str(a[i+1])):
        a1.append(a[i]+a[i+1])
print(len(a1),min(a1))