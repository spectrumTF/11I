from fnmatch import*
f=[str(x) for x in open('17-346.txt')]
k=[]
for i in range(len(f)-2):
    proizv=1
    for u in range(3):
        for j in range(len(f[i+u])-1):
            #print(str(f[i+u])[j])
            a=int(str(f[i+u])[j])
            proizv*=a
    if proizv<=2*10**9 and fnmatch(str(proizv),'83*8*'):
        k.append(proizv)
print(len(k),max(k))