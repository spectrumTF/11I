with open('17-4.txt') as f:
    a=[int(x) for x in f.readlines()]
a1=[]
sr=sum(a)/len(a)
for i in range(len(a)-1):  
    if (a[i]<sr or a[i+1]<sr) and ((a[i]%7==0 and a[i]%3!=0 and a[i]%11!=0 and abs(a[i])%13!=0) or (a[i+1]%7==0 and a[i+1]%3!=0 and a[i+1]%11!=0 and a[i+1]%13!=0)):
        a1.append(a[i]+a[i+1])
print(len(a1),min(a1))