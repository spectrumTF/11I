a=[int(x) for x in open('17-257.txt')]
b=[x for x in a if x%2==0]
c=[x for x in a if x%2!=0]
if max(b)>max(c):
    print(len(b),min(b))
else:
    print(len(c),min(c))