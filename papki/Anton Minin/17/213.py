n=[int(x) for x in open('17-1.txt')]
a=[]
for i in range(len(n)-1):
    s=sum(n)/len(n)
    if (n[i]>s and n[i+1]>s) and (n[i]+n[i+1])%100==31:
        a.append((n[i]+n[i+1]))
print(len(a),max(a))
