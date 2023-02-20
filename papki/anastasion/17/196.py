s=[int(x) for x in open('17-10.txt')]
a=[]
for i in range(len(s)-2):
    if ((s[i]**2+s[i+1]**2==s[i+2]**2) or (s[i+1]**2+s[i+2]**2==s[i]**2) or s[i]**2+s[i+2]**2==s[i+1]**2):
        a.append(max(s[i],s[i+1],s[i+2]))
print(len(a),sum(a))