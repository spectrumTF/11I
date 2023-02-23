n=[int(x) for x in open('17-1.txt')]
a=[]
for i in range(len(n)-1):
    s=sum(n)/len(n)
    if (n[i]>s or n[i+1]>s) and (abs(n[i])%10==3 or abs(n[i+1])%10==3):
        a.append((n[i]+n[i+1]))
print(len(a),max(a))
