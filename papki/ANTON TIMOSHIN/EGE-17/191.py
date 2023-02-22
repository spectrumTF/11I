with open("17-7.txt") as f:
    s = list(map(int, f.readlines()))

a = []
for i in range(len(s)):
    if s[i] % 16 == 9 and (s[i]//16) % 16 != 10:
        a.append(s[i])

print(len(a), max(a))
