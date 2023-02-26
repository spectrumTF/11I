with open("17-1.txt") as f:
    a = [int(x) for x in f]
count=0
c = []
s = sum(a)/len(a)
for i in range(len(a)-2):
    if (a[i]<s or a[i+1]<s or a[i+2]<s) and ((a[i]%7==0 and a[i+1]%7==0)or(a[i]%7==0 and a[i+2]%7==0)or(a[i+2]%7==0 and a[i+1]%7==0)):
        count+=1
        c.append(a[i]+a[i+1]+a[i+2])
print(count,max(c))