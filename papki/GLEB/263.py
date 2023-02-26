with open("17-243.txt") as f:
    a = [int(x) for x in f]
s = 0
for x in a:
    if x%33==0:
        for i in str(x):
            s+=int(i)
count = 0
c = []
for i in range(len(a)-1):
    if (a[i]>s or a[i]>s) :
        count+=1
        c.append(a[i]+a[i+1])
print(count,min(c))