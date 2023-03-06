import itertools as it
c=0
for x in it.permutations("ВАЙФУ", r = 4):
    s = "".join(x)
    if s[0] != "Й" and s.count("ВФ") == 0 and "ФВ" not in s:
        c+=1
print(c)