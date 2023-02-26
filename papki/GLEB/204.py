with open("17-204.txt") as f:
    a = [int(x) for x in f]
c = []
count=0
for i in range(len(a)-2):
    if not(a[i]>0 and a[i]%10==9) and (a[i+1]>0 and a[i+1]%10==9) and not(a[i+2]>0 and a[i+2]%10==9):
        count+=1
        c.append(a[i]+a[i+1]+a[i+2])
print(count,max(c))