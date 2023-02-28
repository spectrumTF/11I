a=[int(x) for x in open('17-335.txt')]
a1=[]
s=[x for x in a if x%43==0]
m=min(s)
for i in range(len(a)-1):
    if  int((a[i]+a[i+1])%m==0) + int((a[i]%10==m%10 or a[i+1]%10==m%10))==1:
        a1.append(max(a[i],a[i+1]))
print(len(a1),max(a1))