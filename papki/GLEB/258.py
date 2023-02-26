with open("17-257.txt") as f:
    a = [int(x) for x in f]
    b = [int(x) for x in a if x%2==0]
    c = [int(x) for x in a if x%2!=0]
    p = max(b)
    p1 =max(c)
    if p > p1:
        print(len(b),min(b))
    else:
        print(len(c),min(c))