with open("24_1.txt") as f:
    s= f.readline()
    mx=0
    k=0
    for i in range(len(s)):
        if s[i]=="C":
            k+=1
            mx=max(mx,k)
        else:
            k=0
print(mx)