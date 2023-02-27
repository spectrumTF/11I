with open('17-10.txt') as f:
    a=[int(x) for x in f.readlines()]
a1=[]
for i in range(len(a)-1):
    if ((a[i]+a[i+1])//1000==0 and (a[i]+a[i+1])//100>0) and (a[i]+a[i+1])%10>(a[i]+a[i+1])%100//10:
        a1.append(a[i]+a[i+1])
print(len(a1),min(a1))
