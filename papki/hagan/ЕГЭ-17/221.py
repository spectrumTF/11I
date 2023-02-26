s=[int(x) for x in open("17-1.txt")]
a=[]
for i in range(len(s)-1):
    s1=sum(s)/len(s)
    if (s[i]<s1 or s[i+1]<s1) and ((s[i]%3==0 and s[i]%5!=0 and s[i]%11!=0 and s[i]%19!=0) or (s[i+1]%3==0 and s[i+1]%5!=0 and s[i+1]%11!=0 and s[i+1]%19!=0)):
        a.append(s[i]+s[i+1])
print(len(a),max(a))