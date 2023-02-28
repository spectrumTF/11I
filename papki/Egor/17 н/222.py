a=[int(x) for x in open('17-4.txt')]
b=[]
sr=sum(a)/len(a)
for i in range(len(a)-1):
         if (a[i]<sr or a[i+1]<sr) and ((abs(a[i])%7==0 and abs(a[i])%3!=0 and abs(a[i])%11!=0 and abs(a[i])%13!=0) or (abs(a[i+1])%7==0 and abs(a[i+1])%3!=0 and abs(a[i+1])%11!=0 and abs(a[i+1])%13!=0)):
                  b.append ((a[i]+a[i+1]))
print(len(b),min(b))