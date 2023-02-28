a=[int(x) for x in open('17-1.txt')]
b=[]
sr=sum(a)/len(a)
for i in range(len(a)-1):
   if (abs((a[i]>sr) or abs(a[i+1]>sr)) and abs((a[i]%17==0) or (a[i+1])%17==0)):
         b.append ((a[i]+a[i+1]))
print(len(b),max(b))