s=[int(x) for x in open("17-243.txt")]
a=[]
b=[x for x in s if x%153==0]
m=max(b)
for i in range(len(s)-1):
    s1=bin(s[i])[2:]
    s2=bin(s[i+1])[2:]    
    if (s[i]>m or s[i+1]>m) and (s1.count("1111")>=1 or s2.count("1111")>=1):
            a.append(s[i]+s[i+1])
print(len(a),min(a))