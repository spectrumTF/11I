with open('17-302.txt') as f:
    a=[int(x) for x in f.readlines()]
a1=[]
s=[x for x in a if x%21==0]
for i in range(len(a)-1):
    if int(abs((a[i]+a[i+1])/2-min(s))**0.5)==abs((a[i]+a[i+1])/2-min(s))**0.5:
        a1.append(a[i]*a[i+1])
print(len(a1),min(a1))