with open("17-4.txt") as f:
    s = list(map(int, f.readlines()))

a = []
for i in range(len(s)):
    if s[i] % 5 == 3 and s[i] % 9 == 5 and s[i] % 8 != 7:
        a.append(s[i])

print(len(a), max(a))
