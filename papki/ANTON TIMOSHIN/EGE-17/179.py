with open("17-4.txt") as f:
    s = list(map(int, f.readlines()))

a = []
for i in range(len(s)):
    if ((s[i] % 10 == 2) or (s[i] % 10 == 7)) and (s[i] % 3 == 0) and (s[i] % 11 == 0):
        a.append(s[i])

print(len(a), min(a))
