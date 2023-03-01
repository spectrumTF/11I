a=[int(x) for x in open('17-288.txt')]
a1=[]
for i in range(len(a)-2):
    if (abs(a[i])%7)!=(abs(a[i+1])%7) and (abs(a[i+1])%7)!=(abs(a[i+2])%7) and (abs(a[i])%7)!=(abs(a[i+2])%7) and (a[i]<0 or a[i+1]<0 or a[i+2]<0):
        a1.append(max(a[i],a[i+1],a[i+2])-min(a[i],a[i+1],a[i+2]))
print(len(a1),min(a1))