a = [int(x) for x in open("17-257.txt")]
b = [int(x) for x in a if x%2==0]
c = [int(x) for x in a if x%2!=0]
z = max(b)
y =max(c)
if z > y:
    print(len(b),min(b))
else:
    print(len(c),min(c))
