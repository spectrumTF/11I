for i in range(1000):
    n = i
    if n % 2 != 0:
        n = "10" + bin(n)[2:] + "11"
    else:
        n = "1" + bin(n)[2:] + "00"
    r = int(n, 2)
    if r > 1023:
        print(r)
        break


