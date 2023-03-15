with open("24_19.txt") as f:
    s= f.readline()
    s=s.replace("O","A")
    s=s.replace("C","B")
    s=s.replace("D","B")
    s=s.split(" ")
    mx=0
    k=0
    for i in range(len(s)-1):
        if s[i]+s[i+1]=="BA":
            k+=1
            mx=max(mx,k)
        else:
            k=0
print(k)