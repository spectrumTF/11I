a=[int(x) for x in open('17-328.txt')]
a1=[]
s=[x for x in a if x%50==0]
for i in range(len(a)-2):
    a2=[str(a[i]+a[i+1]),str(a[i]+a[i+2]),str(a[i+1]+a[i+2])]
    if a2[0]==a2[0][::-1] and a2[1]==a2[1][::-1] and a2[2]==a2[2][::-1] and max(int(a2[0]),int(a2[1]),int(a2[2]))<max(s) :
        a1.append(a[i]+a[i+1]+a[i+2])
print(len(a1),max(a1))