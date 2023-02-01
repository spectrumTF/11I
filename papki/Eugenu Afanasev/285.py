
for n in range(10000):
    x=bin(n)[2:]
    if n%2==0:
        x=x+'10'
    else:
        x='1'+x+'01'
    r=int(x,2)
    if r>516:
        print(n)
        break
    