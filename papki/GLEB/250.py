with open("17-243.txt") as f:
    a = [int(x) for x in f]
    b = [z for z in a if z%171==0]
count=0
c = []
s = max(b)
for i in range(len(a)-1):
    if (a[i]>s or a[i+1]>s) and (str(a[i]).count("11")>=1 or str(a[i+1]).count("11")>=1):
        count+=1
        c.append(a[i]+a[i+1])
print(count,min(c))