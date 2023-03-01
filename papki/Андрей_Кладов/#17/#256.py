a=[int(x) for x in open('17-243.txt')]
a1=[]
s=[x for x in a if x%107==0]
m=max(s)
for i in range(len(a)-1):
    x=a[i]
    c=''
    while x!=0:
        c+=str(x%7)
        x//=7
    x1=a[i+1]
    c1=''
    while x1!=0:
        c1+=str(x1%7)
        x1//=7
    if (a[i]>m or a[i+1]>m) and ('36' in c[::-1] or '36' in c1[::-1]):
        a1.append(a[i]+a[i+1])
print(len(a1),min(a1))