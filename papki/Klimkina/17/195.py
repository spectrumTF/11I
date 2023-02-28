a=[int(x) for x in open('17-9.txt')]
b=[bin(x)[2:] for x in a]
a1=[]
for i in range(len(a)-2):
    if (int(b[i].count('1')>=3 and b[i].count('0')>=1)+int(b[i+1].count('1')>=3 and b[i+1].count('0')>=1)+int(b[i+2].count('1')>=3 and b[i+2].count('0')>=1))>=2:
        a1.append(max(a[i],a[i+1],a[i+2]))
print(len(a1),max(a1))