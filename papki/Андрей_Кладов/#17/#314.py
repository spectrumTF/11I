a=[int(x) for x in open('17-304.txt')]
a1=[]
s=[x for x in a if x%246==0]
a2=[hex(x)[2:] for x in a]
for i in range(len(a)-1):
    if 'aa' in a2[i]  and 'aa' in a2[i+1] and (a[i]+a[i+1])<max(s):
        a1.append(a[i]+a[i+1])
print(len(a1),max(a1))