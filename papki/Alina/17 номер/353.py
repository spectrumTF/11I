with open('17-353.txt') as f:
    a=[int(x) for x in f.readlines()]
a1=[]
sr=(max(a)+min(a))/2
for i in range(len(a)//2+1):
    if (a[i]<sr and a[len(a)-1-i]>sr) or (a[i]>sr and a[len(a)-1-i]<sr):
        a1.append(a[i]+a[len(a)-1-i])
print(len(a1),max(a1))