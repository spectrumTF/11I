a=[int(x) for x in open('17-4.txt')]
a1=[]
sr=sum(a)/len(a)
for i in range(len(a)-1):
    if (a[i]<sr or a[i+1]<sr) and (not ('5' in str(a[i])) or not ('5' in str(a[i+1]))) :
        a1.append(a[i]+a[i+1])
print(len(a1),min(a1))