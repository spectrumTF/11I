with open("17-257.txt") as f:
    a = [int(x) for x in f]
    b = [int(x) for x in a if x%11==0]
    c = [int(x) for x in a if x%17==0]
    if len(b) > len(c):
        print(len(b),min(b))
    else:
        print(len(c),max(c))