a=[int(x) for x in open('17-297.txt')]
a1=[]
s=[int(str(x)[-1:]) for x in a]
s1=[x for x in a if x%51==0]
for i in range(len(a)-1):
    if (int(a[i]==s[i]*51) + int(a[i+1]==s[i+1]*51))==1  and a[i]+a[i+1]<max(s1):
        a1.append(a[i]+a[i+1])
print(len(a1),max(a1))