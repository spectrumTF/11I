with open("17-4.txt") as f:
    s = list(map(int, f.readlines()))

a = []
for i in range(len(s)):
    b = str(s[i])
    if b.count("0") >= 2 and s[i] % 7 == 0:
        a.append(s[i])

print(max(a), len(a))