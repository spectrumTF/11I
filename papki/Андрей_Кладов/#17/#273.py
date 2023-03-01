a=[int(x) for x in open('17-273.txt')]
a1=[]
a2=[]
for i in range(len(a)-2):
    if (a[i]+a[i+1]+a[i+2])<max(a) :
        a1.append(max(a[i],a[i+1],a[i+2]))
        a2.append(min(a[i],a[i+1],a[i+2]))
print(len(a1),max(a1)+min(a2))