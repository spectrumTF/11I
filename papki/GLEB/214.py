with open("17-4.txt") as f:
    a = [int(x) for x in f]
count=0
c = []
s = sum(a)/len(a)
for i in range(len(a)-1):
    if (a[i]<s and a[i+1]<s) and (a[i]+a[i+1])%100==19:
        count+=1
        c.append(a[i]+a[i+1])
print(count,min(c))