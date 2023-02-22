with open('17-296.txt') as f:
    a=[int(x) for x in f.readlines()]   
a1=[]
s=[int(str(abs(x))[:1]) for x in a]
for i in range(len(a)-1):
    if a[i]*a[i+1]>sum(s):
        a1.append(a[i]+a[i+1])
print(len(a1),max(a1))