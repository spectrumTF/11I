n=[int(x) for x in open('17-205.txt')]
a=[]
for i in range(len(n)-1):
    if (abs(n[i])%100==17 or abs(n[i+1])%100==17) and abs(n[i]+n[i+1])%2==0:
        a.append((n[i]+n[i+1]))
print(len(a),max(a))
