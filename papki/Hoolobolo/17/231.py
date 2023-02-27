a=[int(x)for x in open('17_1.txt')]
b=sum(a)/len(a)
c=[]
for i in range(len(a)-2):
    if (a[i]<b or a[i+1]<b or a[i+2]<b) and ((abs(a[i])%10==4 and abs(a[i+1])%10==4) or (abs(a[i+1])%10==4 and abs(a[i+2])%10==4)or (abs(a[i])%10==4 and abs(a[i+2])%10==4)) :
        c.append(a[i]+a[i+1]+a[i+2])
print(len(c),max(c))