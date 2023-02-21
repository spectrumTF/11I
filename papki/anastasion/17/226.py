s=[int(x) for x in open('17-4.txt')]
a=[]
for i in range(len(s)-1):
    b=sum(s)/len(s)
    if (s[i]<b or s[i+1]<b) and (str(s[i]).count('4')==0 and str(s[i+1]).count('4')==0):
        a.append((s[i]+s[i+1]))
print(len(a),min(a))