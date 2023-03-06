import itertools as it
c=0
for x in it.permutations("ИГРОК"):
    s = "".join(x)
    if s[0]!='К' and "РОК" not in s :
        c+=1
print(c)