a=[int(x) for x in open('17-1.txt')]
b=[]
sr=sum(a)/len(a)
for i in range(len(a)-1):
   if (a[i]>sr or a[i+1]>sr) and (abs(a[i])%10==3 or abs(a[i+1])%10==3):
         b.append ((a[i]+a[i+1]))
print(len(b),max(b))