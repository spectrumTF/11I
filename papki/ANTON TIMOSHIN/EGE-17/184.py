with open("17-5.txt") as f:
    s = list(map(int, f.readlines()))

count = 0
mx = 0
for i in range(len(s) - 1):
    if abs(s[i]) % 2 == 0 or abs(s[i+1]) % 2 == 0:
        count += 1
        mx = max(mx, s[i] + s[i+1])

print(count, mx)
