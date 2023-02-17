with open("17-4.txt") as f:
    s = list(map(int, f.readlines()))

a = []
for i in range(len(s)):
    if int((s[i] % 2 == 0) + (s[i] % 3 == 0) + (s[i] % 5 == 0) + (s[i] % 7 == 0)) == 2:
        a.append(s[i])

print(len(a), max(a) + min(a))

