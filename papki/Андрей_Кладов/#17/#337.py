a=[int(x) for x in open('17-336.txt')]
a1=[]
s=[x for x in a if x%37==0]
m=max(s)
for i in range(len(a)-1):
    if  (a[i]%m==0 or a[i+1]%m==0) and (a[i]+a[i+1])%m>30:
        a1.append(a[i]+a[i+1])
print(len(a1),min(a1))