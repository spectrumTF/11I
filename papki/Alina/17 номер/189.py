with open('17-7.txt') as f:
    a=[int(x) for x in f.readlines()]   
a1=[]
for i in range(len(a)-2):
    if (int(a[i]%3==2) + int(a[i+1]%3==2) + int(a[i+2]%3==2))>=1:
        a1.append(min(a[i],a[i+1],a[i+2]))
print(len(a1),sum(a1))  