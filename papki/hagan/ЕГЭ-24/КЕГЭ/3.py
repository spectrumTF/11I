with open("24_3.txt") as f:
    s= f.readline()
    s=s.split("D")
    mx=0
    for i in range(len(s)):
        mx=max(mx,len(s[i]))
print(mx)