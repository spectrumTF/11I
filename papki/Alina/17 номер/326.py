with open('17-324.txt') as f:
    a=[int(x) for x in f.readlines()]
a1=[]
def f(x):
    c=''
    while x!=0:
        c+=str(x%5)
        x//=5
    return c==c[::-1]
a2=[x for x in a if x%31==0]
sr=sum(a2)/len(a2)
for i in range(len(a)-2):
    sr1=(a[i]+a[i+1]+a[i+2])/3
    if f(a[i]+a[i+1]+a[i+2])==True and sr1>sr :
        a1.append(a[i]+a[i+1]+a[i+2])
print(len(a1),min(a1))