with open('17-1.txt') as f:
    a=[int(x) for x in f.readlines()]
a1=[]
sr=sum(a)/len(a)
for i in range(len(a)-1):  
    if (a[i]<sr and a[i+1]>sr) or (a[i]>sr and a[i+1]<sr):
        a1.append(a[i]+a[i+1])
print(len(a1),max(a1))