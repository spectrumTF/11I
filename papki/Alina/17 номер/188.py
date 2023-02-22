with open('17-7.txt') as f:
    a=[int(x) for x in f.readlines()]
s=[hex(x)[2:] for x in a]    
a1=[]
for i in range(len(s)-2):
    if (int(s[i][-1:]=='0') + int(s[i+1][-1:]=='0') + int(s[i+2][-1:]=='0'))>=2:
        a1.append(max(a[i],a[i+1],a[i+2]))
print(len(a1),sum(a1))  