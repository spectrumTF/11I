c=0
for x in range(100000000,200000001):
    i=x
    n=0
    while x!=0:
        n+=x%10
        x//=10
    a=bin(n)[2:]
    if a.count('1')%2==0:
        a='1'+a+'00'
    else:
        a='10'+a+'1'
    r=int(a,2)
    if r==21:
        c+=1
        print(i)
print(c)