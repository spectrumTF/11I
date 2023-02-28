a=[int(x) for x in open('17-9.txt')]
b=[bin(x)[2:] for x in a]
c=[]
for i in range(len(a)-2):
    if (b[i].count('1')==2 and b[i+1].count('1')==2 and b[i].count('0')>=1 and b[i+1].count('0')>=1) or (b[i].count('1')==2 and b[i+2].count('1')==2 and b[i].count('0')>=1 and b[i+2].count('0')>=1) or (b[i+1].count('1')==2 and b[i+2].count('1')==2 and b[i+1].count('0')>=1 and b[i+2].count('0')>=1):
        c.append(max(a[i],a[i+1],a[i+2]))
        print(len(c),sum(c))
