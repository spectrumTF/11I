a = [int(x) for x in open("17-1.txt")]
c = []
s = sum(a)/len(a)
for i in range(len(a)-1):
    if (a[i]<s and a[i+1]>s) or (a[i]>s and a[i+1]<s) :
        c.append((a[i]+a[i+1]))
print(len(c),max(c))
