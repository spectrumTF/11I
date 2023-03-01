def f(x):
    c=''
    while x!=0:
        c+=str(x%6)
        x//=6
    return c[::-1]
a=[int(x) for x in open('17-290.txt')]
a1=[]
for i in range(len(a)-2):
    if (a[i]%5==4 or a[i+1]%5==4 or a[i+2]%5==4) and (not('0' in f(a[i]))) and (not('0' in f(a[i+1]))) and (not ('0' in f(a[i+2]))) and a[i]>0 and a[i+1]>0 and a[i+2]>0:
        a1.append(max(a[i],a[i+1],a[i+2])-min(a[i],a[i+1],a[i+2]))
print(len(a1),max(a1))