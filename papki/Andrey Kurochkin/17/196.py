a=[int(x) for x in open('17-10.txt')]
b=[]
for i in range(len(s)-2):
    if ((a[i]**2+a[i+1]**2==a[i+2]**2) or (a[i+1]**2+a[i+2]**2==a[i]**2) or a[i]**2+a[i+2]**2==a[i+1]**2):
        b.append(max(a[i],a[i+1],a[i+2]))
print(len(b),sum(b))
