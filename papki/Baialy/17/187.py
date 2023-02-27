with open('17-6.txt') as f:
    a=[int(x) for x in f.readlines()]
s=[bin(x)[2:] for x in a]    
a1=[]
for i in range(len(s)-2):
    if s[i].count('1')==s[i+1].count('1')==s[i+2].count('1')==3:
        a1.append(max(a[i],a[i+1],a[i+2]))
print(len(a1),sum(a1))  
