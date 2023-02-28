a=[int(x) for x in open('17-4.txt')]
b=[]
sr=sum(a)/len(a)
for i in range(len(a)-1):
         if (a[i]<sr or a[i+1]<sr) and ('1' in str(a[i]) and '1' in str(a[i+1])):
                  b.append ((a[i]+a[i+1]))
print(len(b),min(b))