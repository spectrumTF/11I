a=[int(x) for x in open('17-4.txt')]
a1=[]
for i in range(len(a)-1):
    s=sum(a)/len(a)
    if (a[i]<s or a[i+1]<s) and (str(a[i]).count('4')==0 and str(a[i+1]).count('4')==0):
        a1.append(a[i]+a[i+1])
print(len(a1),min(a1))