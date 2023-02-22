with open('17-243.txt') as f:
    a=[int(x) for x in f.readlines()]
a1=[]
s1=[bin(x)[2:] for x in a]
s=[x for x in a if x%153==0]
m=max(s)
for i in range(len(a)-1):
    if (a[i]>m or a[i+1]>m) and ('1111' in str(s1[i]) or '1111' in str(s1[i+1])):
        a1.append(a[i]+a[i+1])
print(len(a1),min(a1))      