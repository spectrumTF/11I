a=[int(x) for x in open('17-1.txt')]
a1=[]
for i in range(len(a)-2):
    s=sum(a)/len(a)
    if (a[i]<s or a[i+1]<s or a[i+2]<s) and (str(a[i]).count('8')>=1 or str(a[i+1]).count('8')>=1 or str(a[i+2]).count('8')>=1):
        a1.append(a[i]+a[i+1]+a[i+2])
print(len(a1),max(a1))