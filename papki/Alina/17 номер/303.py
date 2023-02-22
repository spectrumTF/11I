with open('17-303.txt') as f:
    a=[int(x) for x in f.readlines()]
a1=[]
a2=[]
s=[x for x in a if round(x**(1/3))**3==x]
m=max(s)
for i in range(len(a)-2):
    if abs(m-a[i]-a[i+1]-a[i+2])%2==0 and int((abs(m-a[i]-a[i+1]-a[i+2]))**0.5)==((abs(m-a[i]-a[i+1]-a[i+2]))**0.5):
        a1.append((a[i]*a[i+1]*a[i+2])//max(a[i],a[i+1],a[i+2]))
        a2.append(a[i]+a[i+1]+a[i+2])
print(len(a1),a1[a2.index(max(a2))])
