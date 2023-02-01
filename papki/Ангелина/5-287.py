c = 0
for i in range(10000):
    n = bin(i) [2:]
    if i%2 == 0:
        n = '1' + n + '11' 
    else:
        n = '11' + n + '0'
    r = int(n, 2)
    if 500<=r<=1000:
        c+=1 
print(c)