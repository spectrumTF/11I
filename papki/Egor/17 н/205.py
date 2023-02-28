a=[int(x) for x in open('17-205.txt')]
b=[]
for i in range(len(a)-1):
    if abs((a[i]-a[i+1])%2==0) and ((a[i]-a[i+1])%37==0):
        b.append ((a[i]+a[i+1]))
print(len(b),max(b))