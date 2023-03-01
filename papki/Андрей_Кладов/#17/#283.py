a=[int(x) for x in open('17-282.txt')]
a1=[]
s=[x for x in a if x%13==0]
for i in range(len(a)-1):
    if a[i]%max(s)==0 or a[i+1]%max(s)==0 :
        a1.append(a[i]+a[i+1])
print(len(a1),min(a1))