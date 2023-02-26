s=[int(x) for x in open("17-8.txt")]
a=[]
for i in range(len(s)-1):
    if (bin(s[i])[2:].count("1")>5 and bin(s[i])[2:].count("1")%2!=0) or (bin(s[i+1])[2:].count("1")>5 and bin(s[i+1])[2:].count("1")%2!=0):
        a.append(s[i]+s[i+1])
print(len(a),max(a))