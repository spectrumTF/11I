s=[int(x) for x in open('17-257.txt')]
a=[x for x in s if x%11==0]
b=[x for x in s if x%17==0]
if len(a)>len(b):
    print(len(a),min(a))
else:
    print(len(b),max(b))