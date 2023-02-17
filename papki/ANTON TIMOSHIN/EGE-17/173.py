with open("17-4.txt") as f:
    s = list(map(int, f.readlines()))

a = []
for i in range(len(s)):
    if (s[i] % 3 == 0) and (s[i] % 9 != 0) and (s[i] % 10 >= 4):
        a.append(s[i])

print(len(a), sum(a)//len(a))
