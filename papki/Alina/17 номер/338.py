with open('17-338.txt') as f:
    a=[int(x) for x in f.readlines()]
a1=[]
for i in range(len(a)-1):
    if  (a[i]%117==min(a) or a[i+1]%117==min(a)):
        a1.append(a[i]+a[i+1])
print(len(a1),max(a1))