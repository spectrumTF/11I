s=[int(x) for x in open("17-243.txt")]
a=[]
b=[x for x in s if x%119==0]
m=max(b)
for i in range(len(s)-1):
    if s[i]<m and s[i+1]<m:
            a.append(s[i]+s[i+1])
print(len(a),max(a))