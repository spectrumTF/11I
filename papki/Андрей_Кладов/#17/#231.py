a=[int(x) for x in open('17-1.txt')]
a1=[]
sr=sum(a)/len(a)
for i in range(len(a)-2):
    if (a[i]<sr or a[i+1]<sr or a[i+2]<sr) and (int(abs(a[i])%10==4) + int(abs(a[i+1])%10==4) + int(abs(a[i+2])%10==4))>=2:
        a1.append(a[i]+a[i+1]+a[i+2])
print(len(a1),max(a1))