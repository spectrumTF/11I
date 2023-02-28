a=[int(x) for x in open('17-339.txt')]
a1=[]
s=[x for x in a if x>0 and x%19==0]
for i in range(len(a)-1):
    if  a[i]+a[i+1]<min(s):
        a1.append(a[i]+a[i+1])
print(len(a1),max(a1))