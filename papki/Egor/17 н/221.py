a=[int(x) for x in open('17-1.txt')]
b=[]
sr=sum(a)/len(a)
for i in range(len(a)-1):
         if (a[i]<sr or a[i+1]<sr) and ((abs(a[i])%3==0 and abs(a[i])%5!=0 and abs(a[i])%11!=0 and abs(a[i])%19!=0) or (abs(a[i+1])%3==0 and abs(a[i+1])%5!=0 and abs(a[i+1])%11!=0 and abs(a[i+1])%19!=0)):
                  b.append ((a[i]+a[i+1]))
print(len(b),max(b))