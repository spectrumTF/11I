s=[int(x) for x in open('17-4.txt')]
a=[]
for i in range(len(s)-1):
    s1=sum(s)/len(s)
    if (s[i]<s1 or s[i+1]<s1) and ((s[i]%7==0 and s[i]%3!=0 and s[i]%11!=0 and s[i]%13!=0) or (s[i+1]%7==0 and s[i+1]%3!=0 and s[i+1]%11!=0 and s[i+1]%13!=0)):
        a.append(s[i]+s[i+1])
print(len(a),min(a))