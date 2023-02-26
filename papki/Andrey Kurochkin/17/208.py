a = [int(x) for x in open("17-205.txt")]
count=0
c = []
for i in range(len(a)-1):
    if( abs(a[i])%100==17 or abs(a[i+1])%100==17 ) and abs(a[i]+a[i+1])%2==0:
        count+=1
        c.append(a[i]+a[i+1])
print(count,max(c))
