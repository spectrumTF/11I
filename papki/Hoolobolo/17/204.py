a=[int(x) for x in open('17_204.txt')]
b=[]
for i in range(len(a)-2):
    if (a[i+1]>0 and a[i+1]%10==9):
        b.append(a[i]+a[i+1]+a[i+2])
print(len(b),max(b))