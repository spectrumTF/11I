def F(b):
    if (b.count('1') == 2) and (b.count('0') > 0): return 1
    else: return 0
f=open('17-9.txt')
a=[int(i) for i in f]
k=0
m=-1000000
s=[]
for i in range(len(a)-2):
    b=bin(a[i])[2:]
    c=bin(a[i+1])[2:]
    d=bin(a[i+2])[2:]
    if F(b)+F(c)+F(d)>=2:
        k+=1
        s.append(max(a[i],a[i+1],a[i+2]))
print(k,sum(s))