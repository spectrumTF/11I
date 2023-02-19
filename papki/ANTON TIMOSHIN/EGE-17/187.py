with open("17-6.txt") as f:
    s = list(map(int, f.readlines()))

count = 0
mx = 0
for i in range(1, len(s) - 1):
    if bin(s[i-1]).count("1") == 3 and bin(s[i]).count("1") == 3 and bin(s[i+1]).count("1") == 3:
        count += 1
        mx += max(s[i-1], s[i], s[i+1])

print(count, mx)
