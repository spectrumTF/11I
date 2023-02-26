s=[int(x) for x in open("17-1.txt")]
a=[]
for i in range(len(s)-1):
    s1=sum(s)/len(s)
    if (s[i]<s1 or s[i+1]<s1) and (abs(s[i])%100==13 or abs(s[i+1])%100==13):
        a.append(s[i]+s[i+1])
print(len(a),max(a))