a=[int(x) for x in open('17-292.txt')]
a1=[]
for i in range(len(a)-1):
    if abs((a[i]%17)-(a[i+1]%17))==((a[i]%4)+(a[i+1]%4)):
        a1.append(a[i]+a[i+1])
print(len(a1),min(a1))