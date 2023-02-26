a = [int(x) for x in open("17-243.txt")]
b = [z for z in a if z%119==0]
c = []
s = max(b)
for i in range(len(a)-1):
    if (a[i]<s and a[i+1]<s):
        c.append(a[i]+a[i+1])
print(len(c),max(c))
