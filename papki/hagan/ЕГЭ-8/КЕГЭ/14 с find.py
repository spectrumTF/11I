import itertools as it
c=0
for x in it.permutations("ДЕЙКСТРА", r = 6):
    s = "".join(x)
    if s.count("Й") == 1 and s[-1] != "Й" and s[s.find("Й") + 1] in "ДКСТР":
        c+=1
print(c)