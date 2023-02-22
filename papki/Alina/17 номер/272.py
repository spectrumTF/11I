with open('17-272.txt') as f:
    a=[int(x) for x in f.readlines()] 
a1=[]
s=[x for x in a if x>0]
sr=sum(s)/len(s)
for i in range(len(a)-1):
    x=abs(a[i])
    c=0
    while x!=0:
        c+=x%10
        x//=10
    x1=abs(a[i+1])
    c1=0
    while x1!=0:
        c1+=x1%10
        x1//=10        
    if a[i]>sr or a[i+1]>sr :
        a1.append(max(c,c1))
print(len(a1),max(a1))        