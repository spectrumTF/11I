with open("17-243.txt") as f:
    a = [int(x) for x in f]
    b = [z for z in a if z%111==0]
count=0
c = []
s = max(b)
for i in range(len(a)-1):
    if (a[i]>s or a[i+1]>s) and (a[i]%10==7 or a[i+1]%10==7):
        count+=1
        c.append(a[i]+a[i+1])
print(count,min(c))