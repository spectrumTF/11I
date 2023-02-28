a=[int(x) for x in open('17-1.txt')]
a1=[]
for i in range(len(a)-2):
    s=sum(a)/len(a)
    if (a[i]<s or a[i+1]<s or a[i+2]<s) and (abs(a[i])%10==6 or abs(a[i+1])%10==6 or abs(a[i+2])%10==6):
        a1.append(a[i]+a[i+1]+a[i+2])
print(len(a1),max(a1))