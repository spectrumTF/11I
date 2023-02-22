with open('17-257.txt') as f:
    a=[int(x) for x in f.readlines()] 
a1=[]    
s=[x for x in a if x%2==1]
for i in range(len(a)-1):
    if a[i]+a[i+1]>max(s)+min(s) and (a[i]+a[i+1])%2==0:
        a1.append(a[i]+a[i+1])
print(len(a1),min(a1))        