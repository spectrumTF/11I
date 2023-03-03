a=[int(x) for x in open('17-257.txt')]
b=[x for x in a if x%7==0]
c=[x for x in a if x%13==0]
if min(b)>min(c):
    print(len(b),max(b))
else:
    print(len(c),max(c))