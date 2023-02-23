s=[int(x) for x in open('17-243.txt')]
a=[]
b=[x for x in s if x%111==0]
c=max(b)
for i in range(len(s)-1):
    if (s[i]>c or s[i+1]>c) and (s[i]%10==7 or s[i+1]%10==7):
        a.append(s[i]+s[i+1])
print(len(a),min(a))