with open('17-294.txt') as f:
    a=[int(x) for x in f.readlines()]   
a1=[]
def f(x):
    c=0
    while x!=0:
        c+=x%10
        x//=10
    return c
sr=sum(a)/len(a)
for i in range(len(a)-1):
    if int((f(a[i])+f(a[i+1]))**0.5)==(f(a[i])+f(a[i+1]))**0.5 and a[i]+a[i+1]>sr:
        a1.append(f(a[i])+f(a[i+1]))
print(len(a1),max(a1))