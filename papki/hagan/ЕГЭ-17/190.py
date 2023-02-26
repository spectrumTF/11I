s=[int(x) for x in open("17-7.txt")]
a=[]
for x in s:
    if x%8==7 and x//8%8!=2:
        a.append(x)
print(len(a),max(a))