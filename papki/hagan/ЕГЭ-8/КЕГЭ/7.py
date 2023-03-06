import itertools as it
c=0
for x in it.permutations("ABIKOLYN"):
    s = "".join(x)
    Ok = True
    for i in range(len(s)-1):
        if (s[i] in "AIOY") == (s[i + 1] in "AIOY") :
            Ok=False
            break
    if Ok==True:
        c+=1
print(c)