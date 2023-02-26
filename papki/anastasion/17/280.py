s=[int(x) for x in open('17-278.txt')]
a=[]
b=[oct(x)[2:].count('7') for x in s]
for i in range(len(s)-1):
    if (s[i]>sum(b)*7 and s[i+1]>sum(b)*7):
        a.append(s[i]+s[i+1])
print(len(a),min(a))