s=[int(x) for x in open("17-7.txt")]
a=[]
for x in s:
    if x%16==9 and x//16%16!=10:
        a.append(x)
print(len(a),max(a))