with open("17-1.txt") as f:
    a = [int(x) for x in f]
count=0
c = []
s = sum(a)/len(a)
for i in range(len(a)-1):
    if a[i]>s or a[i+1]>s:
        count+=1
        c.append(a[i]+a[i+1])
print(count,max(c))