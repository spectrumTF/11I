with open('17-10.txt') as f:
    a=[int(x) for x in f.readlines()]
a1=[]
for i in range(len(a)-1):
    x=a[i]+a[i+1]
    c=''
    while x!=0:
        c+=str(x%7)
        x//=7      
    if c[::-1]==c:
        a1.append(int(c[::-1]))
print(len(a1),max(a1))