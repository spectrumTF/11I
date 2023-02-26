def d(x):
    a=0
    while x > 0:
        if x%10==5:
            a+=1
        x//=10
    if a!=0:
        return 1
    else:
        return 0



with open("17-4.txt") as f:
    a = [int(x) for x in f]
count=0
c = []
s = sum(a)/len(a)
for i in range(len(a)-1):
    if (a[i]<s or a[i+1]<s) and (d(a[i])==0 or d(a[i+1])==0):
        count+=1
        c.append(a[i]+a[i+1])
print(count,min(c))