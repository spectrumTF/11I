a=[int(x) for x in open('17-257.txt')]
s=[x for x in a if x%7==0]
s1=[x for x in a if x%13==0]
if min(s)>min(s1):
    print(len(s),max(s))
else:
    print(len(s1),max(s1))