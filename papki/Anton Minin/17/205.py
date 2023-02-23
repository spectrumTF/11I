n=[int(x) for x in open('17-205.txt')]
a=[]
for i in range(len(n)-1):
    if abs(n[i+1]-n[i])%2==0 and abs(n[i+1]-n[i])%37==0:
        a.append((n[i]+n[i+1]))
print(len(a),max(a))
