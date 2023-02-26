s=[int(x) for x in open("17-205.txt")]
a=[]
for i in range(len(s)-1):
    if abs(s[i+1]-s[i])%2==0 and abs(s[i+1]-s[i])%37==0:
        a.append((s[i]+s[i+1]))
print(len(a),max(a))