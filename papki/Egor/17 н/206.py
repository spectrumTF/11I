a=[int(x) for x in open('17-205.txt')]
b=[]
for i in range(len(a)-1):
    if abs(((a[i]%7==0) or (a[i+1]%7==0)) and (a[i]+a[i+1])%5==0):
        b.append ((a[i]+a[i+1]))
print(len(b),max(b))