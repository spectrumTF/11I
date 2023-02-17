s=[int(x) for x in open('17-7.txt')]
a=[]
for i in range(len(s)):
    if s[i]%16==9 and s[i]//16%16!=10:
        a.append((s[i]))
print(len(a),max(a))