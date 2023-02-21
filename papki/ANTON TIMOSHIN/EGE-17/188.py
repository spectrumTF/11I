with open("17-7.txt") as f:
    s = list(map(int, f.readlines()))

count = 0
mx = 0
for i in range(1, len(s) - 1):
    if (s[i-1] % 16 == 0) + (s[i] % 16 == 0) + (s[i+1] % 16 == 0) >= 2:
        count += 1
        mx += max(s[i-1], s[i], s[i+1])

print(count, mx)
