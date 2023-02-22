with open('17-243.txt') as f:
    a=[int(x) for x in f.readlines()] 
a1=[]    
s=[x for x in a if x%35==0]
c=0
for i in range(len(s)):
    x=s[i]
    while x!=0:
        c+=x%10
        x//=10
for i in range(len(a)-1):
    if (a[i]<c and a[i+1]>c and hex(a[i])[-2:]=='ef') or (a[i]>c and a[i+1]<c and hex(a[i+1])[-2:]=='ef'):
        a1.append(a[i]+a[i+1])
print(len(a1),min(a1))        