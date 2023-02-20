s=[int(x) for x in open('17-4.txt')]
a=[]
for i in range(len(s)-1):
    b=sum(s)/len(s)
    if (s[i]<b and s[i+1]<b) and (s[i]+s[i+1])%100==19:
        a.append((s[i]+s[i+1]))
print(len(a),min(a))