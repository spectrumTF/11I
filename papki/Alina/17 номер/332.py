with open('17-332.txt') as f:
    a=[int(x) for x in f.readlines()]
a1=[]
s=[x for x in a if x%17==0]
sr=sum(s)/len(s)
def f(x):
    c=0
    while x!=0:
        c+=x%10
        x//=10
    return c 
for i in range(len(a)-2):
    if  f(a[i])==f(a[i+2]) and a[i+1]<sr:
        a1.append(f(a[i+1]))
a2={i:a1.count(i) for i in set(a1)}
for i in set(a2):
    if a2[i]==max(a2.values()):
        print(len(a1),i)