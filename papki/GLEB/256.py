def g(x):
    n = ""
    k = ""
    while x>0 :
        n = n + str(x%7)
        x //= 7
    n = list(reversed(n))
    for i in range(len(n)):
        k += n[i]
    return k

with open("17-243.txt") as f:
    a = [int(x) for x in f]
    b = [int(x) for x in a if x%107==0]
count=0
c = []
s = max(b)
for i in range(len(a)-1):
    if (a[i]>s or a[i+1]>s) and (g(a[i]).count("36")>=1 or g(a[i+1]).count("36")>=1):
        count+=1
        c.append(a[i]+a[i+1])
print(count,min(c))