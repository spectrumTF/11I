with open("17-4.txt") as f:
    s = list(map(int, f.readlines()))

a = []
for i in range(len(s)):
    if ((s[i] // 10) % 10 <= 4) and (3 <= ((s[i]) // 100) % 10 <= 7):
        a.append(s[i])

print(len(a), min(a))
