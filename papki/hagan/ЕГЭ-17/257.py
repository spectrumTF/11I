s=[int(x) for x in open('17-257.txt')]
m1=[x for x in s if x%7==0]
m2=[x for x in s if x%13==0]
if min(m1)>min(m2):
    print(len(m1),max(m2))
else:
    print(len(m2),max(m2))