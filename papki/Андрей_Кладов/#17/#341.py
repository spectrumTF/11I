f=[int(x) for x in open('17-341.txt')]
sr=sum(f)/len(f)
ksu=[]
ksr=[]
for i in range(len(f)-3):
    if f[i+1]*f[i+2]>f[i]*f[i+3]:
        ksu.append(f[i+1]+f[i+2])
        if f[i+1]>sr or f[i+2]>sr:
            ksr.append(1)
print(max(ksu),len(ksr))