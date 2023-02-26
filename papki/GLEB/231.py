with open("17-1.txt") as f:
    a = [int(x) for x in f]
count=0
c = []
s = sum(a)/len(a)
for i in range(len(a)-2):
    if (a[i]<s or a[i+1]<s or a[i+2]<s) and ((abs(a[i])%10==4 and abs(a[i+1])%10==4)or(abs(a[i])%10==4 and abs(a[i+2])%10==4)or(abs(a[i+2])%10==4 and abs(a[i+1])%10==4)):
        count+=1
        c.append(a[i]+a[i+1]+a[i+2])
print(count,max(c))