with open('17-328.txt') as f:
    a=[int(x) for x in f.readlines()]
a1=[]
s=[x for x in a if x%2==1]
sr=sum(s)/len(s)
for i in range(len(a)-2):
    a2=[a[i]+a[i+1],a[i]+a[i+2],a[i+1]+a[i+2]]
    if not('7' in oct(a2[0])[2:]) and not('7' in oct(a2[1])[2:]) and not('7'in oct(a2[2])[2:]) and a[i]+a[i+1]+a[i+2]<sr:
        a1.append(a[i]+a[i+1]+a[i+2])
print(len(a1),max(a1))