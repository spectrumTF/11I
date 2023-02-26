with open("17-257.txt") as f:
    a = [int(x) for x in f]
    b = [int(x) for x in a if x%10==4]
s = min(b)+max(b)
count = 0
c = []
for i in range(len(a)-1):
    if (a[i]+a[i+1])<s:
        count+=1
        c.append(a[i]+a[i+1])
print(count,max(c))