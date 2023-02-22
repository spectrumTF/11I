with open("17-7.txt") as f:
    s = list(map(int, f.readlines()))

a = []
for i in range(len(s)):
    b = s[i]
    n = 0
    while s[i]:
        n += s[i] % 10
        s[i] //= 10
    if n % 3 == 0:
        a.append(b)

print(len(a), max(a))

