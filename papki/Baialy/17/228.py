with open('17-1.txt') as f:
    a=[int(x) for x in f.readlines()]
a1=[]
sr=sum(a)/len(a)
for i in range(len(a)-2):     
    if (a[i]<sr or a[i+1]<sr or a[i+2]<sr) and (abs(a[i])%3==0 or abs(a[i+1])%3==0 or abs(a[i+2])%3==0):
        a1.append(a[i]+a[i+1]+a[i+2])
print(len(a1),max(a1))
