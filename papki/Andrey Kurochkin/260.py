a = [int(x) for x in open("17-257.txt")]
b = [int(x) for x in a if x%10==4]
s = min(b)+max(b)
c = []
for i in range(len(a)-1):
    if (a[i]+a[i+1])<s:
        c.append(a[i]+a[i+1])
print(len(c),max(c))
