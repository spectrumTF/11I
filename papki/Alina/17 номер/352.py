with open('17-352.txt') as f:
    a=[int(x) for x in f.readlines()]
a1=[]
s=[x for x in a if x%73==0]
for i in range(len(a)-1):
    if a[i]>=max(s) and a[i+1]>=max(s):
        a1.append(a[i]+a[i+1])
print(len(a1),max(a1))