n=[int(x) for x in open('17-4.txt')]
a=[]
for i in range(len(n)-1):
    s=sum(n)/len(n)
    if (n[i]<s or n[i+1]<s) and (str(n[i]).count('7')>=1 or str(n[i+1]).count('7')>=1):
        a.append((n[i]+n[i+1]))
print(len(a),min(a))
