a=[int(x) for x in open('17-292.txt')]
a1=[]
for i in range(len(a)-1):
    if ((a[i]%6)+(a[i+1]%6))==((a[i]%11)+(a[i+1]%11)):
        a1.append(a[i]+a[i+1])
print(len(a1),max(a1))