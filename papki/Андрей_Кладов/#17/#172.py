a=[int(x) for x in open('17-4.txt')]
b=[bin(x)[2:] for x in a]
s=[]
for i in range(len(a)):
    if b[i][-4:]=='1001' and a[i]%5==1 and (a[i]//5)%5==1:
        s.append(a[i])
print(max(s),sum(s))