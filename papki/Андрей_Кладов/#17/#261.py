a=[int(x) for x in open('17-257.txt')]
a1=[]
s=[x for x in a if x%2==1]
for i in range(len(a)-1):
    if (a[i]+a[i+1])*2>max(s):
        a1.append(a[i]+a[i+1])
print(len(a1),min(a1))