with open('17-278.txt') as f:
    a=[int(x) for x in f.readlines()]
a1=[]    
s=[oct(x)[2:].count('7') for x in a]
for i in range(len(a)-1):
    if a[i]>sum(s)*7 and a[i+1]>sum(s)*7 :
        a1.append(a[i]+a[i+1])
print(len(a1),min(a1))  