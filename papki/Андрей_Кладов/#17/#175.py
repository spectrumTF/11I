a=[int(x) for x in open('17-4.txt')]
#b=[bin(x)[2:] for x in a]
s=[]

for i in range(len(a)):
    x=a[i]
    z = ''
    c = 0
    while x > 0:
        z = z + str(x % 10)
        x = x // 10
    while x > 0:
        c += x % 10
        x = x // 10
    if c%5==0 and z[-2:]!='00':
        s.append(a[i])
print(len(s),max(s))