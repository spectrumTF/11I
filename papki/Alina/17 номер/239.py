with open('17-1.txt') as f:
    a=[int(x) for x in f.readlines()]
a1=[]
sr=sum(a)/len(a)
for i in range(len(a)-2):
    if (int(a[i]<sr) + int(a[i+1]<sr) + int(a[i+2]<sr))>=2 and (int(abs(a[i])%10==8) + int(abs(a[i+1])%10==8) + int(abs(a[i+2])%10==8))>=2:
        a1.append(a[i]+a[i+1]+a[i+2])
print(len(a1),max(a1))        