import itertools as it
c=0
for x in it.product("ЕЛМРУ",repeat=4):
    s = "".join(x)
    c+=1
    if s[0] == "Л":
        print(c)    
        break