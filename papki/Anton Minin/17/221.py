n=[int(x) for x in open('17-1.txt')]
a=[]
for i in range(len(n)-1):
    s=sum(n)/len(n)
    if (n[i]<s or n[i+1]<s) and ((n[i]%3==0 and n[i]%5!=0 and n[i]%11!=0 and n[i]%19!=0) or (n[i+1]%3==0 and n[i+1]%5!=0 and n[i+1]%11!=0 and n[i+1]%19!=0)):
        a.append((n[i]+n[i+1]))
print(len(a),max(a))
