import itertools as it
c=0
for x in it.product("BILHA",repeat = 6):
    s = "".join(x)
    if s.count("B")<=1 and s[0] not in "L" and s[-1] not in "IA" :
        c+=1
print(c)