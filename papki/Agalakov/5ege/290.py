a =[]
k= 0
for i in range(100000000,1000000000):
    sum = 0
    while (i != 0):
        sum = sum + i % 10
        i = i // 10
    n = bin(sum)[2:]
    if n.count('1')%2==0:
        n = '1' + n + '00'
    else:
        n = '10' + n + '1'
    r = int(n,2)
    if r==21:
        k +=1
        print(k)
        #по сути должно работать гыгыггы
