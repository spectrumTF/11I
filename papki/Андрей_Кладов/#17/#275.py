a=[int(x) for x in open('17-275.txt')]
a1=[]
for i in range(len(a)-1):
    if abs(a[i]+a[i+1])%11==0:
        a1.append(a[i]+a[i+1])
print(len(a1),max(a1))