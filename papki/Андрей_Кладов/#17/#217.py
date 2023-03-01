a=[int(x) for x in open('17-1.txt')]
a1=[]
sr=sum(a)/len(a)
for i in range(len(a)-1):
    if (a[i]<sr or a[i+1]<sr) and (abs(a[i])%100==13 or abs(a[i+1])%100==13):
        a1.append(a[i]+a[i+1])
print(len(a1),max(a1))