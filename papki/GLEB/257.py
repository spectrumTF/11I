with open("17-257.txt") as f:
    a = [int(x) for x in f]
    b = [int(x) for x in a if x%7==0]
    c = [int(x) for x in a if x%13==0]
    p = min(b)
    p1 = min(c)
    if p > p1:
        print(len(b),max(b))
    else:
        print(len(c),max(c))