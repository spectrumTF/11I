import itertools as it
c = с1 = 0
for x in it.product("АИМРЯ",repeat=4):
    s = "".join(x)
    c += 1
    if s == "АРИЯ":   
        c1 = c
print(c1)