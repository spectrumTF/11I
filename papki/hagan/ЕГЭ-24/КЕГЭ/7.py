with open("24_7.txt") as f:
    s= f.readline()
    s=s.replace("XY","X Y")
    s=s.replace("XZ","X Z")
    s=s.split(" ")
    mx=0
    for i in range(len(s)):
        mx=max(mx,len(s[i]))
print(mx)