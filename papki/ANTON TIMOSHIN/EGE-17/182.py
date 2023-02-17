with open('17-4.txt') as f:
    s = list(map(int, f.readlines()))

a = []
for i in range(len(s)):
    if (s[i] % 13 == 7) and (s[i] % 7 != 0) and (s[i] % 11 != 0):
        a.append(s[i])

print(max(a) - min(a), len(a))
