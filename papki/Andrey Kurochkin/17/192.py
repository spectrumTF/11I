a=[int(x) for x in open('17.txt')]
b=[]
for i in range(len(a)):
    x=a[i]
    k=0
    while x:
        k+=x%10
        x=x//10
    if k%3==0:
        b.append(a[i])
        print(len(b),max(b))
        
    
