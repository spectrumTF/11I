a=[int(x) for x in open('17-278.txt')]
a1=[]
s=[x for x in a if x%12==0]
c=''
for i in range(len(s)):
    x=s[i]
    while x!=0:
        c+=str(x%5)
        x//=5
for i in range(len(a)-1):
    if a[i]>c.count('4')*4 and a[i+1]>c.count('4')*4:
        a1.append(a[i]+a[i+1])
print(len(a1),max(a1))