a = [int(x) for x in open("17-1.txt")]
c=[]
b=sum(a)/len(a)
for i in range(len(a)-2):
    if (a[i]<b or a[i+1]<b or a[i+2]<b) and (str(a[i]).count('8')>=1 or str(a[i+1]).count('8')>=1 or str(a[i+2]).count('8')>=1):
        c.append((a[i]+a[i+1]+a[i+2]))
print(len(c),max(c))
