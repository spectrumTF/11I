import itertools as it
c=0
for x in it.product("ЛОДКА",repeat = 4):
    s = "".join(x)
    if s.count("О")>=2:
        c+=1
print(c)