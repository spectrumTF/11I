c=0
for n in range(1000,10000):
    n=str(n)
    if int(n[0])%2==0:
        s=int(n[0])+int(n[2])+abs(int(n[1])-int(n[3]))
    if int(n[0])%2!=0:
        r=sorted(n)
        r=int(''.join(r))
        r=bin(r)[2:]
        s=r.count('1')
    if s>20:
        c+=1
print(c)

# работает