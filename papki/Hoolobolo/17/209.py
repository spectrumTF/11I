a=[int(x) for x in open('17_205.txt')]
b=[]
for i in range(len(a)-1):
        if (abs(a[i])%7==0 or (abs(a[i+1])%7==0)) and (abs(a[i]+a[i+1])%100==19):
                b.append(a[i]+a[i+1])
print(len(b),max(b))