a = [int(x) for x in open("17-243.txt")]
b = [z for z in a if z%171==0]
c = []
s = max(b)
for i in range(len(a)-1):
    if (a[i]<s or a[i+1]<s) and (a[i]%2!=0 or a[i+1]%2!=0):
        c.append(a[i]+a[i+1])
print(len(c),max(c))
