s=[int(x) for x in open('17-288.txt')]
a=[]
for i in range(len(s)-2):
    if ((abs(s[i])%7)!=(abs(s[i+1])%7) and (abs(s[i+1])%7)!=(abs(s[i+2])%7) and (abs(s[i])%7)!=(abs(s[i+2])%7)) and (s[i]<0 or s[i+1]<0 or s[i+2]<0):
        a.append(max(s[i],s[i+1],s[i+2])-min(s[i],s[i+1],s[i+2]))
print(len(a),min(a))