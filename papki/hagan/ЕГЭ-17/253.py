s=[int(x) for x in open("17-243.txt")]
a=[]
b=[x for x in s if x%127==0]
m=max(b)
for i in range(len(s)-1):
    if (s[i]>m or s[i+1]>m) and (oct(s[i]).count('31')>=1 or oct(s[i+1]).count('31')>=1):
            a.append(s[i]+s[i+1])
print(len(a),min(a))