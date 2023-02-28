a=[int(x) for x in open('17-4.txt')]
b=[]
sr=sum(a)/len(a)
for i in range(len(a)-1):
   if (abs((a[i]>sr) or abs(a[i+1]>sr)) and (a[i]+a[i+1])%7==0):
         b.append ((a[i]+a[i+1]))
print(len(b),min(b))