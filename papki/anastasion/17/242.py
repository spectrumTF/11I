s=[int(x) for x in open('17-1.txt')]
a=[]
for i in range(len(s)-2):
    b=sum(s)/len(s)
    if ((s[i]<b and s[i+1]<b) or (s[i+2]<b and s[i]<b) or (s[i+2]<b and s[i+1]<b)) and (str(s[i]).count('1')>=1 and str(s[i+1]).count('1')>=1 and str(s[i+2]).count('1')>=1):
        a.append((s[i]+s[i+1]+s[i+2]))
print(len(a),max(a))