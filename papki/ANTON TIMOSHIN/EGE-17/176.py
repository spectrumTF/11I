with open("17-4.txt") as f:
    s = list(map(int, f.readlines()))

a = []
count = 0
for i in range(len(s)):
    b = s[i] % 10 + (s[i] // 10) % 10
    if (b >= 15) and (s[i] % 3 != 0) and (s[i] % 4 != 0) and (s[i] % 7 != 0):
        a.append(s[i])

print(min(a), sum(a))
