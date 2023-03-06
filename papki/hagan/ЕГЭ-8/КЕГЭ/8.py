import itertools as it
c=0
for x in it.product("AB123",repeat = 8):
    s = "".join(x)
    if s.count("A") + s.count("B")==2:
        c+=1
print(c)