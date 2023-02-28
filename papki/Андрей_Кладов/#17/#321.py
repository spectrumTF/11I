a=[int(x) for x in open('17-316.txt')]
a1=[]
sr=sum(a)/len(a)
def f(x,y):
    return int((x+y)**0.5)==(x+y)**0.5
for i in range(len(a)-2):
    sr1=(a[i]+a[i+1]+a[i+2])/3
    if (f(a[i],a[i+1])==True or f(a[i+2],a[i+1])==True or f(a[i],a[i+2])==True) and sr1>sr :
        a1.append(a[i]+a[i+1]+a[i+2])
print(len(a1),max(a1))