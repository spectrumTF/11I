import itertools as it
c=0
for x in it.product("КРЕСЛО",repeat = 4):
    s = "".join(x)
    if s[0] in "КРСЛ" and s[-1] in "ЕО":
        c+=1
print(c)