a = [int(x) for x in open("17-257.txt")]
b = [int(x) for x in a if x%7==0]
c = [int(x) for x in a if x%13==0]
z = min(b)
y = min(c)
if z > y:
    print(len(b),max(b))
else:
    print(len(c),max(c))
