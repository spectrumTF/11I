a=[int(x) for x in open('17-205.txt')]
a1=[]
for i in range(len(a)-1):
    if abs(a[i+1]-a[i])%2==0 and abs(a[i+1]-a[i])%37==0:
        a1.append(a[i]+a[i+1])
print(len(a1),max(a1))