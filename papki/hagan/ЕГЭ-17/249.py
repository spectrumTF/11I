s=[int(x) for x in open("17-243.txt")]
a=[]
b=[x for x in s if x%211==0]
m=max(b)
for i in range(len(s)-1):
    if (s[i]>m or s[i+1]>m) and (str(s[i]).count("1")>=1 or str(s[i+1]).count("1")>=1):
            a.append(s[i]+s[i+1])
print(len(a),min(a))