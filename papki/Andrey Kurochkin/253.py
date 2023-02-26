a = [int(x) for x in open("17-243.txt")]
b = [z for z in a if z%127==0]
c = []
s = max(b)
for i in range(len(a)-1):
    if (a[i]>s or a[i+1]>s) and (oct(a[i]).count("31")>=1 or oct(a[i+1]).count("31")>=1):
        c.append(a[i]+a[i+1])
print(len(c),min(c))
