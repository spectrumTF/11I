import itertools as it
c=0
for x in it.product("ABCWXYZ",repeat = 6):
    s = "".join(x)
    if s[0] in "WXYZ" and s[-1] in "WXYZ" and s[1] in "ABC" and s[2] in "ABC" and s[3] in "ABC" and s[4] in "ABC":
        c+=1
print(c)