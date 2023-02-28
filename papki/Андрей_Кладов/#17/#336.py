a=[int(x) for x in open('17-336.txt')]
a1=[]
a2=[]
s=[x for x in a if x%8==0 and x!=8]
m=min(s)
for i in range(len(a)-1):
    if  a[i]%m==0 and a[i+1]%m==0:
        a1.append(max(a[i],a[i+1]))
        a2.append(a[i]+a[i+1])
print(len(a1),a1[a2.index(min(a2))])