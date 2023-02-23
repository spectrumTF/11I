n=[int(x) for x in open('17-205.txt')]
a=[]
for i in range(len(n)-1):
    if (abs(n[i])%7==0 or abs(n[i+1])%7==0) and abs(n[i]+n[i+1])%100==19:
        a.append((n[i]+n[i+1]))
print(len(a),max(a))
