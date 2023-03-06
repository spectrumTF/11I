import itertools as it
c = с1 = 0
for x in it.product("АГИЛМОРТ",repeat=4):
    s = "".join(x)
    c += 1
    if s[-2:] == "ИМ":   
        c1 = c
print(c1)