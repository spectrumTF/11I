with open('17-205.txt') as f:
    a=[int(x) for x in f.readlines()]
a1=[]
for i in range(len(a)-1):  
    if (abs(a[i])%10==7 or abs(a[i+1])%10==7) and abs(a[i]+a[i+1])%12==0 :
        a1.append(a[i]+a[i+1])
print(len(a1),max(a1))
