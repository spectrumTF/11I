a=[int(x) for x in open('17-4.txt')]
b=[]
sr=sum(a)/len(a)
for i in range(len(a)-1):
   if (a[i]<sr and a[i+1]<sr) and ((a[i])%100==19 or (a[i+1])%100==19):
         b.append ((a[i]+a[i+1]))
print(len(b),max(b))