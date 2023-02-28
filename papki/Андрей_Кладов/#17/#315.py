a=[int(x) for x in open('17-304.txt')]
a1=[]
sr=sum(a)/len(a)
for i in range(len(a)-1):
    if '101010' in bin(a[i]*a[i+1])[2:] and (a[i]+a[i+1])>sr:
        a1.append(a[i]+a[i+1])
print(len(a1),min(a1))