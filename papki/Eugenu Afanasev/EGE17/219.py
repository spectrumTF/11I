a = [int(x) for x in open("17-4.txt")]
c = []
s = sum(a)/len(a)
for i in range(len(a)-1):
    if (a[i]<s and a[i+1]<s) and ((a[i])%10==9 or (a[i+1])%10==9)  :
        c.append((a[i]+a[i+1]))
print(len(c),max(c))
