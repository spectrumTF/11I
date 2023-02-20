s=[int(x) for x in open('17-1.txt')]
a=[]
for i in range(len(s)-1):
    b=sum(s)/len(s)
    if (s[i]>b or s[i+1]>b) and (abs(s[i])%10==3 or abs(s[i+1])%10==3):
        a.append((s[i]+s[i+1]))
print(len(a),max(a))