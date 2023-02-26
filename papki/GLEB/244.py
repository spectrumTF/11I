with open("17-243.txt") as f:
    a = [int(x) for x in f]
    b = [z for z in a if z%119==0]
count=0
c = []
s = max(b)
for i in range(len(a)-1):
    if (a[i]<s and a[i+1]<s):
        count+=1
        c.append(a[i]+a[i+1])
print(count,max(c))