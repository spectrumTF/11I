with open("17-10.txt") as f:
    a = [int(x) for x in f]
count=0
c = []
for i in range(len(a)-2):
    if (a[i]**2 + a[i+1]**2 == a[i+2]**2) or (a[i]**2 + a[i+2]**2 == a[i+1]**2) or (a[i+2]**2 + a[i+1]**2 == a[i]**2):
        count+=1
        c.append(max(a[i],a[i+1],a[i+2]))
print(count,sum(c))