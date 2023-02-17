with open("17-4.txt") as f:
    s = list(map(int, f.readlines()))

a = []
for i in range(len(s)):
    if (bin(s[i])[-4::] == "1001") and (s[i] % 5 == 1) and ((s[i] // 5) % 5 == 1):
        a.append(s[i])

print(max(a), sum(a))
