with open('17-342.txt') as f:
    a=[int(x) for x in f.readlines()]
a1=[]
s=[x for x in a if x%37==0]
s1=[x for x in a if x%73==0]
for i in range(len(a)-1):
    if  (int(a[i] in range(max(s1)+1,min(s))) + int(a[i+1] in range(max(s1)+1,min(s))))==1:
        a1.append(a[i]+a[i+1])
print(len(a1),min(a1))