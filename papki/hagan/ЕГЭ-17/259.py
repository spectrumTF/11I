s=[int(x) for x in open('17-257.txt')]
m1=[x for x in s if x%11==0]
m2=[x for x in s if x%17==0]
if len(m1)>len(m2):
    print(len(m1),min(m1))
else:
    print(len(m2),min(m2))