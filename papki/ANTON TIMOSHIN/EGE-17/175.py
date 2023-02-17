with open("17-4.txt") as f:
    s = list(map(int, f.readlines()))

a = []
count = 0

for i in range(len(s)):
    x = s[i]
    count = 0
    for n in str(s[i]):
        count += int(n)
    if count % 5 == 0 and (count % 5 == 0) and (str(s[i])[2:] != "00"):
        a.append(s[i])
print(len(a), max(a))


