with open("17-10.txt") as f:
    a = [int(x) for x in f]
count=0
c = []
for i in range(len(a)-1):
    if 1000 >a[i]+a[i+1] >= 100 and ((a[i]+a[i+1])%10 > ((a[i]+a[i+1])//10)%10):
        count+=1
        c.append(a[i]+a[i+1])
print(count,min(c))
        