with open("17-205.txt") as f:
    a = [int(x) for x in f]
count=0
c = []
for i in range(len(a)-1):
    if( abs(a[i])%7==0 or abs(a[i+1])%7==0 ) and abs(a[i]+a[i+1])%5==0:
        count+=1
        c.append(a[i]+a[i+1])
print(count,max(c))