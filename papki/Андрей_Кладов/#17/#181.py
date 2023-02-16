a=[int(x) for x in open('17-4.txt')]
#b=[bin(x)[2:] for x in a]
s=[]
for i in range(len(a)):
    if (a[i]%10==5 or a[i]%10==7) and a[i]%9!=0 and a[i]%11!=0:
        s.append(a[i])
print(len(s),max(s)+min(s))