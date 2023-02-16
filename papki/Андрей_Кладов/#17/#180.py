a=[int(x) for x in open('17-4.txt')]
#b=[bin(x)[2:] for x in a]
s=[]
for i in range(len(a)):
    if a[i]%5==3 and a[i]%9==5 and a[i]%8!=7:
        s.append(a[i])
print(len(s),max(s))