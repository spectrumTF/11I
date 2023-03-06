import itertools as it
c=0
for x in it.product("123456789",repeat=3):
    s = "".join(x)
    if s[0]>=s[1]>=s[2]:
        c+=1
print(c)