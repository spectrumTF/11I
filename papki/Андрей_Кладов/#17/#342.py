f=[int(x) for x in open('17-342.txt')]
f37=[int(x) for x in f if x%37==0]
f73=[int(x) for x in f if x%73==0]
k=[]
mi37=min(f37)
for i in range(len(f)-1):
    if int(min(f37)>f[i]>max(f73))+int(min(f37)>f[i+1]>max(f73))==1:
        k.append(f[i]+f[i+1])
print(len(k),min(k))