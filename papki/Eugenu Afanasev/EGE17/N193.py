n=[int(x) for x in open('17-9.txt')]
b=[bin(x)[2:] for x in n]
c=[]
for i in range(len(n)-2):
    if (int(b[i].count('1')==2 and b[i].count('0')>=1) + int(b[i+1].count('1')==2 and b[i+1].count('0')>=1) or int(b[i+2].count('1')==2 and b[i+2].count('0')>=1))==2:
        c.append(n[i]+n[i+1]+n[i+2])
print(len(c),max(c))
