with open('17-4.txt') as f:
    a=[int(x) for x in f.readlines()]
a1=[]
for i in range(len(a)):
    if a[i]%13==7 and a[i]%7!=0 and a[i]%11!=0:
        a1.append(a[i])
print(max(a1)-min(a1),len(a1))  
