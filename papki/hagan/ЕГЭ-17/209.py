s=[int(x) for x in open('17-205.txt')]
a=[]
for i in range(len(s)-1):
    if (abs(s[i])%7==0 or abs(s[i+1])%7==0) and abs(s[i]+s[i+1])%100==19:
        a.append((s[i]+s[i+1]))
print(len(a),max(a))