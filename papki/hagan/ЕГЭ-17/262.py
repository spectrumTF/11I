s=[int(x) for x in open('17-257.txt')]
a=[]
m=[x for x in s if x%2!=0]
for i in range(len(s)-1):
    if (s[i]+s[i+1])%2==0 and (s[i]+s[i+1])>(max(m)+min(m)):
        a.append(s[i]+s[i+1])
print(len(a),min(a))