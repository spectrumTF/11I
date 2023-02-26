with open("17-1.txt") as f:
    a = [int(x) for x in open("17-1.txt")]
c = []
s = sum(a)/len(a)
for i in range(len(a)-1):
    if (a[i]<s or a[i+1]<s) and (abs(a[i])%100==13 or abs(a[i+1])%100==13)  :
        c.append((a[i]+a[i+1]))
print(len(c),max(c))
