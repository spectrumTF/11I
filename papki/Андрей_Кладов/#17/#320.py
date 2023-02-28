a=[int(x) for x in open('17-316.txt')]
a1=[]
s=[x for x in a if x%202==0]
def f(x,y):
    return x%2==0 and y%2==0 and (x+y)%100==44
for i in range(len(a)-2):
    if (f(a[i],a[i+1])==True or f(a[i+2],a[i+1])==True or f(a[i],a[i+2])==True) and a[i]+a[i+1]+a[i+2]>max(s) :
        a1.append(a[i]+a[i+1]+a[i+2])
print(len(a1),min(a1))