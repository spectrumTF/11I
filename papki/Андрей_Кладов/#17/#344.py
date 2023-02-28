f=[int(x) for x in open('17-344.txt')]
f103=[int(x) for x in f if x%103==0]
k=[]
mi103=min(f103)
for i in range(len(f)-1):
    if (f[i]+f[i+1])%2==0 and abs(f[i]-f[i+1])%mi103==0:
        k.append(f[i]+f[i+1])
print(len(k),max(k))