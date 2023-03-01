a=[int(x) for x in open('17-257.txt')]
s=[x for x in a if x%11==0]
s1=[x for x in a if x%17==0]
if len(s)>len(s1):
    print(len(s),min(s))
else:
    print(len(s1),max(s1))