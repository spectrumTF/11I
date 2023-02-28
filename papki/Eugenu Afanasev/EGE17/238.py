a = [int(x) for x in open("17-1.txt")]
c = []
s = sum(a)/len(a)
for i in range(len(a)-2):
    if ((a[i]<s and a[i+1]<s) or (a[i+2]<s and a[i+1]<s) or (a[i]<s and a[i+2]<s)) and (abs(a[i])%100==14 or abs(a[i+1])%100==14 or abs(a[i+2])%100==14):
        c.append(a[i]+a[i+1]+a[i+2])
print(len(c),max(c))
