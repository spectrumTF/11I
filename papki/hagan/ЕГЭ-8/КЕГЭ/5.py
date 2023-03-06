import itertools as it
c=0
for x in it.product("САЛО",repeat = 6):
    s = "".join(x)
    if 1<=s.count("О")<=3:
        c+=1
print(c)