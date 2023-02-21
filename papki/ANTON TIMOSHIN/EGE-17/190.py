with open("17-7.txt") as f:
    s = list(map(int, f.readlines()))

a = []
for i in range(len(s)):
    if s[i] % 8 == 7 and (s[i] // 8) % 8 != 2:
        a.append(s[i])

print(len(a), max(a))
