a=[int(x) for x in open('17-202.txt')]
a1=[]
for i in range(len(a)-2):
    if a[i+1] in range(100,1000) and a[i+1]%10==5 and (not (a[i] in range(100,1000)) or a[i]%10!=5) and (not (a[i+2] in range(100,1000)) or a[i+2]%10!=5):
        a1.append(a[i]+a[i+1]+a[i+2])
print(len(a1),max(a1))