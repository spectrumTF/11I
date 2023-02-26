s=[int(x) for x in open('17-1.txt')]
a=[]
for i in range(len(s)-1):
    s1=sum(s)/len(s)
    if (s[i]>s1 and s[i+1]>s1) and (s[i]+s[i+1])%100==31:
        a.append((s[i]+s[i+1]))
print(len(a),max(a))