with open('17-345.txt') as f:
    a=[int(x) for x in f.readlines()]
a1=[]
s=[x for x in a if x%100==52]
for i in range(len(a)-1):
    if  (int(a[i]<max(s)-min(s))+int(a[i+1]<max(s)-min(s)))==1:
        a1.append(a[i]+a[i+1])
print(len(a1),max(a1))