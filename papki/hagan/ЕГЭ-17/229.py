s=[int(x) for x in open('17-1.txt')]
a=[]
for i in range(len(s)-2):
    s1=sum(s)/len(s)
    if (s[i]<s1 or s[i+1]<s1 or s[i+2]<s1) and (int(s[i]%7==0)+int(s[i+1]%7==0)+int(s[i+2]%7==0)>=2):
        a.append(s[i]+s[i+1]+s[i+2])
print(len(a),max(a))