s=[int(x) for x in open('17-275.txt')]
a=[]
for i in range(len(s)-1):
    if (abs(s[i])+abs(s[i+1]))%11==0:
        a.append(s[i]+s[i+1])
print(len(a),max(a))