a=[int(x) for x in open('17-288.txt')]
a1=[]
for i in range(len(a)-3):
    if (abs(a[i])%10==3 or abs(a[i+1])%10==3 or abs(a[i+2])%10==3 or abs(a[i+3])%10==3) and abs(a[i])%7!=3 and abs(a[i+1])%7!=3 and abs(a[i+2])%7!=3 and abs(a[i+3])%7!=3 :
        a1.append(max(a[i],a[i+1],a[i+2],a[i+3])-min(a[i],a[i+1],a[i+2],a[i+3]))
print(len(a1),min(a1))