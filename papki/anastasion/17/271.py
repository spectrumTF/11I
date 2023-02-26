s=[int(x) for x in open('17-271.txt')]
a=[]
b=[]
c=sum(s)/len(s)
for i in range(len(s)-1):
    if (abs(s[i])%10+abs(s[i+1])%10)==7:
        a.append(s[i]+s[i+1])
        if s[i]<c and s[i+1]<c:
            b.append(s[i]+s[i+1])
print(len(a),max(b))