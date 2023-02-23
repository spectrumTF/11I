n=[int(x) for x in open('17-205.txt')]
a=[]
for i in range(len(n)-1):
    if (abs(n[i])%10==7 or abs(n[i+1])%10==7) and abs(n[i]+n[i+1])%12==0:
        a.append((n[i]+n[i+1]))
print(len(a),max(a))
