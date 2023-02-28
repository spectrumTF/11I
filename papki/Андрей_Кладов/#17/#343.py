f=[str(x) for x in open('17-343.txt')]
fusl=[]
k=[]
for x in f:
    sch=0
    snech=0
    x1=''.join(reversed(x))
    if len(x)>1:
        for i in range(1,len(x1)):
            if i%2==0: sch+=int(x1[i])
            else: snech+=int(x1[i])
        if snech%sch==0: fusl.append(1)
        else: fusl.append(0)
for j in range(len(fusl)-2):
    if (fusl[j]+fusl[j+1]+fusl[j+2])==3:
        k.append(int(f[j])+int(f[j+1])+int(f[j+2]))
print(len(k),min(k))