with open('17-7.txt') as f:
    a=[int(x) for x in f.readlines()]   
a1=[]
for i in range(len(a)):
    if a[i]%16==9 and a[i]//16%16!=10:
        a1.append(a[i])
print(len(a1),max(a1))