with open('17-4.txt') as f:
    a=[int(x) for x in f.readlines()]
a1=[]
for i in range(len(a)):
    if a[i]%5==3 and a[i]%9==5 and a[i]%8!=7:
        a1.append(a[i])
print(len(a1),max(a1))        