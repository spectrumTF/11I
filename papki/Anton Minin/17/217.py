n=[int(x) for x in open('17-1.txt')]
a=[]
for i in range(len(n)-1):
    s=sum(n)/len(n)
    if (n[i]<s or n[i+1]<s) and (abs(n[i])%100==13 or abs(n[i+1])%100==13):
        a.append((n[i]+n[i+1]))
print(len(a),max(a))
