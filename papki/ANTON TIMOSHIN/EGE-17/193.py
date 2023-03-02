with open("17-8.txt") as f:
    s = list(map(int, f.readlines()))

count = 0
mx = 0
for i in range(len(s) - 1):
    k = bin(s[i])
    l = bin(s[i+1])
    if (k.count("1") > 5 and k.count("1") % 2 != 0) or (l.count("1") > 5 and l.count("1") % 2 != 0):
        count += 1
        mx = max(mx, s[i] + s[i+1])

print(count, mx)
