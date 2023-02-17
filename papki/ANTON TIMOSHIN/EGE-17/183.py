with open("17-4.txt") as f:
    s = list(map(int, f.readlines()))

a = []
for i in range(len(s)):
    if (s[i] % 16 == 11) and (s[i] % 7 == 0) and (s[i] % 6 != 0) and (s[i] % 13 != 0) and (s[i] % 19 != 0):
        a.append(s[i])

print(sum(a), len(a))
