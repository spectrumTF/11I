import itertools as it
c=0
for x in it.product("01234",repeat = 6):
    s = "".join(x)
    if s[-1] not in "34" and s[0] not in "01" :
        c+=1
print(c)