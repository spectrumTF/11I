import itertools as it
c=0
for x in it.product("ПУЛЯ",repeat = 6):
    s = "".join(x)
    if s.count("У")==2:
        c+=1
print(c)