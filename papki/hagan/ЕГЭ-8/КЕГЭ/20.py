import itertools as it
c =0
с1 = ""
for x in it.product("АИМРЯ",repeat=4):
    s = "".join(x)
    c += 1
    if c == 211:   
        c1 = s
print(c1)