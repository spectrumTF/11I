import itertools as it
c=0
s1 = set()
for x in it.permutations("МИМИКРИЯ"):
    s = "".join(x)
    s1.add(s)
print(len(s1))