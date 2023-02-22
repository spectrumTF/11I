with open('17-204.txt') as f:
    a=[int(x) for x in f.readlines()]
a1=[]
for i in range(len(a)-2):  
    if a[i+1]%10==9 and (a[i+1]*(-1))<0 and ((a[i]*(-1))>0 or a[i]%10!=9) and ((a[i+2]*(-1))>0 or a[i+2]%10!=9):
        a1.append(a[i]+a[i+1]+a[i+2])
print(len(a1),max(a1))