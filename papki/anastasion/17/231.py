s=[int(x) for x in open('17-1.txt')]
a=[]
for i in range(len(s)-2):
    b=sum(s)/len(s)
    if (s[i]<b or s[i+1]<b or s[i+2]<b) and ((abs(s[i])%10==4 and abs(s[i+1])%10==4) or (abs(s[i])%10==4 and abs(s[i+2])%10==4) or (abs(s[i+2])%10==4 and abs(s[i+1])%10==4)):
        a.append((s[i]+s[i+1]+s[i+2]))
print(len(a),max(a))