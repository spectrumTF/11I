s=[int(x) for x in open('17-1.txt')]
a=[]
for i in range(len(s)-2):
    s1=sum(s)/len(s)
    if (s[i]<s1 or s[i+1]<s1 or s[i+2]<s1) and (str(s[i]).count('8')>=1 or str(s[i+1]).count('8')>=1 or str(s[i+2]).count('8')>=1):
        a.append(s[i]+s[i+1]+s[i+2])
print(len(a),max(a))