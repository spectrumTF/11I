f=[int(x) for x in open('17-345.txt')]
f52=[int(x) for x in f if (str(x)[-2:]=='52') and len(str(x))>1]
razn=max(f52)-min(f52)
k=[]
for i in range(len(f)-1):
    if (f[i]<razn)!=(f[i+1]<razn):
        k.append(f[i]+f[i+1])
print(len(k),max(k))