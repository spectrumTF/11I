with open('17-7.txt') as f:
    a=[int(x) for x in f.readlines()]   
a1=[]
for i in range(len(a)):
    x=a[i]
    c=0
    while x!=0: 
        c+=x%10
        x//=10
    if c%3==0:
        a1.append(a[i])
print(len(a1),max(a1))
