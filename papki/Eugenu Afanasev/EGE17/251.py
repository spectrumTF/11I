a = [int(x) for x in open("17-243.txt")]
b = [z for z in a if z%153==0]
c = []
s = max(b)
for i in range(len(a)-1):
    if (a[i]>s or a[i+1]>s) and (bin(a[i]).count("1111")>=1 or bin(a[i+1]).count("1111")>=1):
        c.append(a[i]+a[i+1])
print(len(c),min(c))
