s=[int(x) for x in open('17-282.txt')]
a=[]
b=[x for x in s if x%17==0]
c=min(b)
for i in range(len(s)-1):
    if (s[i]%c==0 or s[i+1]%c==0):
        a.append(s[i]+s[i+1])
print(len(a),max(a))