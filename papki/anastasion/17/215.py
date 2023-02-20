s=[int(x) for x in open('17-1.txt')]
a=[]
for i in range(len(s)-1):
    b=sum(s)/len(s)
    if (s[i]>b or s[i+1]>b) and (s[i]%17==0 or s[i+1]%17==0):
        a.append((s[i]+s[i+1]))
print(len(a),max(a))