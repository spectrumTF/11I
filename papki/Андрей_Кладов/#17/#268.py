a=[int(x) for x in open('17-243.txt')]
a1=[]
s=[x for x in a if x%49==0]
c=0
for i in range(len(s)):
    x=s[i]
    while x!=0:
        c+=x%10
        x//=10
for i in range(len(a)-1):
    if (a[i]<c and a[i+1]>c and a[i]%10==7) or (a[i]>c and a[i+1]<c and a[i+1]%10==7):
        a1.append(a[i]+a[i+1])
print(len(a1),min(a1))