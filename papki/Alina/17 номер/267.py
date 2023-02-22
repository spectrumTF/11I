with open('17-243.txt') as f:
    a=[int(x) for x in f.readlines()] 
a1=[]    
s=[x for x in a if x%49==0]
c=0
for i in range(len(s)):
    x=s[i]
    while x!=0:
        c+=x%10
        x//=10
for i in range(len(a)-1):
    if (a[i]<c and a[i+1]>c and a[i+1]%13==0) or (a[i]>c and a[i+1]<c and a[i]%13==0):
        a1.append(a[i]+a[i+1])
print(len(a1),max(a1))        