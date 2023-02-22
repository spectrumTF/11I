with open('17-341.txt') as f:
    a=[int(x) for x in f.readlines()]
a1=[]
a2=[]
sr=sum(a)/len(a)
for i in range(1,len(a)-2):
    if  a[i]*a[i+1]>a[i-1]*a[i+2]:
        a1.append(a[i]+a[i+1])
        if a[i]>sr or a[i+1]>sr:
            a2.append(a[i]+a[i+1])
print(max(a1),len(a2))