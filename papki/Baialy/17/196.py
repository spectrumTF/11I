with open('17-10.txt') as f:
    a=[int(x) for x in f.readlines()]
a1=[]
for i in range(len(a)-2):
    if a[i]**2+a[i+1]**2==a[i+2]**2 or a[i]**2+a[i+2]**2==a[i+1]**2 or a[i+2]**2+a[i+1]**2==a[i]**2:
        a1.append(max(a[i],a[i+1],a[i+2]))
print(len(a1),sum(a1))
