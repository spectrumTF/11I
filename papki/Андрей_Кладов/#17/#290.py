def f(x):
    c=''
    while x!=0:
        c+=str(x%6)
        x//=6
    return c[::-1]
a=[int(x) for x in open('17-290.txt')]
a1=[]
for i in range(len(a)-2):
    if (a[i]%5==1 or a[i+1]%5==1 or a[i+2]%5==1) and len(f(a[i]))==4 and len(f(a[i+1]))==4 and len(f(a[i+2]))==4:
        a1.append(max(a[i],a[i+1],a[i+2])-min(a[i],a[i+1],a[i+2]))
print(len(a1),max(a1))