a=[int(x) for x in open('17-7.txt')]
a1=[]
for i in range(len(a)):
    if a[i]%8==7 and a[i]//8%8!=2:
        a1.append(a[i])
print(len(a1),max(a1))