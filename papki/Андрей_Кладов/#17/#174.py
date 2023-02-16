a=[int(x) for x in open('17-4.txt')]
#b=[bin(x)[2:] for x in a]
s=[]
for i in range(len(a)):
    if a[i]>100 and a[i]//10%10<=4 and 2<a[i]//100%10<8:
        s.append(a[i])
print(len(s),min(s))