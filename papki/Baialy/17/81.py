with open('17-4.txt') as f:
    a=[int(x) for x in f.readlines()]
a1=[]
for i in range(len(a)):
    if (a[i]%10==5 or a[i]%10==7) and a[i]%9!=0 and a[i]%11!=0:
        a1.append(a[i])
print(len(a1),max(a1)+min(a1))      
