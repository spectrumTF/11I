s=[int(x) for x in open('17-1.txt')]
a=[]
for i in range(len(s)-2):
    s1=sum(s)/len(s)
    if int(s[i]<s1)+int(s[i+1]<s1)+int(s[i+2]<s1)>=2 and (int(str(s[i]).count('5')>=1)+int(str(s[i+1]).count('5')>=1)+int(str(s[i+2]).count('5')>=1)>=2):
        a.append(s[i]+s[i+1]+s[i+2])
print(len(a),max(a))