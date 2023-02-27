with open('17-4.txt') as f:
    a=[int(x) for x in f.readlines()]
a1=[]
for i in range(len(a)):
    if a[i]%16==11 and a[i]%7==0 and a[i]%6!=0 and a[i]%13!=0 and a[i]%19!=0:
        a1.append(a[i])
print(sum(a1),len(a1))  
