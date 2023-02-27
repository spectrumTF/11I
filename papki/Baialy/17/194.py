with open('17-9.txt') as f:
    a=[int(x) for x in f.readlines()]
s=[bin(x)[2:] for x in a]
a1=[]
for i in range(len(a)-2):
    if (int(s[i].count('1')==2 and s[i].count('0')>=1) + int(s[i+1].count('1')==2 and s[i+1].count('0')>=1) + int(s[i+2].count('1')==2 and s[i+2].count('0')>=1))>=2:
        a1.append(max(a[i],a[i+1],a[i+2]))
print(len(a1),sum(a1))
