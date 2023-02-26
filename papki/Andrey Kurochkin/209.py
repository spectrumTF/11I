a = [int(x) for x in open("17-205.txt")]
c = []
for i in range(len(a)-1):
    if( abs(a[i])%7==0 or abs(a[i+1])%7==0 ) and abs(a[i]+a[i+1])%100==19:
        c.append(a[i]+a[i+1])
print(len(c),max(c))
