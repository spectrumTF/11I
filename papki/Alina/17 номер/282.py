with open('17-282.txt') as f:
    a=[int(x) for x in f.readlines()]
a1=[]    
s=[x for x in a if x%17==0]
for i in range(len(a)-1):
    if a[i]%min(s)==0 or a[i+1]%min(s)==0 :
        a1.append(a[i]+a[i+1])
print(len(a1),max(a1))  