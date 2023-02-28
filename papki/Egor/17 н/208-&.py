a=[int(x) for x in open('17-205.txt')]
b=[]
for i in range(len(a)-1):
    if abs(((a[i]%100==17) or (a[i+1]%100==17)) and abs(a[i]+a[i+1])%2==0):
        b.append ((a[i]+a[i+1]))
print(len(b),max(b))