import itertools as it
c=0
for x in it.product("ГЕПАРД",repeat = 5):
    s = "".join(x)
    if s.count("Г")==1 and s[0] not in "А" and s[-1]!="Е":
        c+=1
print(c)