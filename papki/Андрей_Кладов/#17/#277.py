a=[int(x) for x in open('17-277.txt')]
a1=[]
s=[abs(x) for x in a if abs(x)%60==0]
c=''
for i in range(len(s)):
    x=s[i]
    while x!=0:
        c+=str(x%3)
        x//=3
for i in range(len(a)-1):
    if a[i]>c.count('2')*2 or a[i+1]>c.count('2')*2:
        a1.append(a[i]+a[i+1])
print(len(a1),max(a1))