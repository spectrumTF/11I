with open("17-7.txt") as f:
    s = list(map(int, f.readlines()))

count = 0
mn = 0
for i in range(1, len(s) - 1):
    if s[i-1] % 3 == 2 or s[i] % 3 == 2 or s[i+1] % 3 == 2:
        count += 1
        mn += min(s[i-1], s[i], s[i+1])

print(count, mn)