s=[int(x) for x in open("17-243.txt")]
a=[]
b=[x for x in s if x%171==0]
m=max(b)
for i in range(len(s)-1):
    if (s[i]<m or s[i+1]<m) and (int(s[i]%2!=0) + int(s[i+1]%2!=0))>=1:
            a.append(s[i]+s[i+1])
print(len(a),max(a))