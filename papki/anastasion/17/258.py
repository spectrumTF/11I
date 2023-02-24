s=[int(x) for x in open('17-257.txt')]
a=[x for x in s if x%2==0]
b=[x for x in s if x%2!=0]
if max(a)>max(b):
    print(len(a),min(a))
else:
    print(len(b),min(b))