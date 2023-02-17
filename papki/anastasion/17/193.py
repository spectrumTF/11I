s=[int(x) for x in open('17-8.txt')]
b=[bin(x)[2:] for x in s]
a=[]
for i in range(len(s)-1):
    if (b[i].count('1')>5 and b[i].count('1')%2!=0) or (b[i+1].count('1')>5 and b[i+1].count('1')%2!=0):
        a.append((s[i]+s[i+1]))
print(len(a),max(a))