with open("17-4.txt") as f:
    s = list(map(int, f.readlines()))

a = []
for i in range(len(s)):
    if (s[i] % 3 == s[i] % 5) and ((s[i] % 31 == 0) or (s[i] % 47 == 0) or (s[i] % 53 == 0)):
        a.append(s[i])

print(len(a), min(a))

