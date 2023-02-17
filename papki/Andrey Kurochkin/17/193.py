a=[int(x) for x in open('17.txt')]
b=[bin(x)[2:] for x in a]
c=[]
for i in range(len(a)-1):
    if (b[i].count('1')>5 and b[i].count('1')%2!=0) or (b[i+1].count('1')>5 and b[i+1].count('1')%2!=0): 
        c.append(a[i]+a[i+1])
        print(len(c),max(c))
        
    
