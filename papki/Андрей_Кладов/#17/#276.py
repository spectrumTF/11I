a=[int(x) for x in open('17-276.txt')]
a1=[]
for i in range(len(a)-2):
    a2=[a[i],a[i+1],a[i+2]]
    a2=sorted(a2)
    if (a2[1]//a2[0])*a2[1]==a2[2] and a2[1]//a2[2]!=1:
        a1.append((a2[1]//a2[0])**2)
print(len(a1),max(a1))