s=[int(x) for x in open('17-257.txt')]
a=[x for x in s if x%7==0]
b=[x for x in s if x%13==0]
if min(a)>min(b):
    print(len(a),max(a))
else:
    print(len(b),max(b))