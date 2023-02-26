s=[int(x) for x in open('17-205.txt')]
a=[]
for i in range(len(s)-1):
    if (abs(s[i])%100==17 or abs(s[i+1])%100==17) and abs(s[i]+s[i+1])%2==0:
        a.append(s[i]+s[i+1])
print(len(a),max(a))