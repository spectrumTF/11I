s=[int(x) for x in open('17-9.txt')]
b=[bin(x)[2:] for x in s]
a=[]
for i in range(len(s)-2):
    if (int(b[i].count('1')>=3 and b[i].count('0')>=1)+int(b[i+1].count('1')>=3 and b[i+1].count('0')>=1)+int(b[i+2].count('1')>=3 and b[i+2].count('0')>=1))>=2:
        a.append(max(s[i],s[i+1],s[i+2]))
print(len(a),max(a))