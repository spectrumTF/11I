with open('17-5.txt') as f:
    a=[int(x) for x in f.readlines()]
a1=[]
for i in range(len(a)-1):
    if abs(a[i])%2==0 or abs(a[i+1])%2==0:
        a1.append(a[i]+a[i+1])
print(len(a1),max(a1))  