a=[int(x) for x in open('17-1.txt')]
a1=[]
for i in range(len(a)-1):
    s=sum(a)/len(a)
    if (a[i]>s and a[i+1]>s) and (a[i]+a[i+1])%100==31:
        a1.append(a[i]+a[i+1])
print(len(a1),max(a1))