with open("17-4.txt") as f:
    s = list(map(int, f.readlines()))

a = []
for i in range(len(s)):
    if (s[i] % 13 == 4) and (s[i] % 8 == 1):
        a.append(s[i])

print(max(a), sum(a))


