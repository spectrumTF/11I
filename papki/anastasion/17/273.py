s=[int(x) for x in open('17-273.txt')]
a=[]
b=[]
for i in range(len(s)-2):
    if (s[i]+s[i+1]+s[i+2])<max(s):
        a.append(max(s[i],s[i+1],s[i+2]))
        b.append(min(s[i],s[i+1],s[i+2]))
print(len(a),max(a)+min(b))