n=[int(x) for x in open('17-4.txt')]
a=[]
for i in range(len(n)-1):
    s=sum(n)/len(n)
    if (n[i]<s or n[i+1]<s) and ((n[i]%7==0 and n[i]%3!=0 and n[i]%11!=0 and n[i]%13!=0) or (n[i+1]%7==0 and n[i+1]%3!=0 and n[i+1]%11!=0 and n[i+1]%13!=0)):
        a.append((n[i]+n[i+1]))
print(len(a),min(a))
