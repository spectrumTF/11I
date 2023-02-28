with open('17-202.txt') as f:
    a=[int(x) for x in f.readlines()]
a1=[]
for i in range(len(a)-2):  
    if a[i+1] in range(100,1000) and a[i+1]%100==12 and (not (a[i] in range(100,1000)) or a[i]%100!=12) and (not (a[i+2] in range(100,1000)) or a[i+2]%100!=12):
        a1.append(a[i]+a[i+1]+a[i+2])
print(len(a1),max(a1))
