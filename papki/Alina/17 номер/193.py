with open('17-8.txt') as f:
    a=[int(x) for x in f.readlines()]
s=[bin(x)[2:].count('1') for x in a]
a1=[]
for i in range(len(a)-1):
    if (int(s[i]>5 and s[i]%2==1) +int(s[i+1]>5 and s[i+1]%2==1))>=1:
        a1.append(a[i]+a[i+1])
print(len(a1),max(a1))